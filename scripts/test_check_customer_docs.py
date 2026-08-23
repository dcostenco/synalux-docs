#!/usr/bin/env python3

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("check_customer_docs.py")
SPEC = importlib.util.spec_from_file_location("check_customer_docs", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CustomerDocsGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs_source_en").mkdir()
        (self.root / "README.md").write_text("# Customer guide\n", encoding="utf-8")
        (self.root / "docs_source_en/guide.md").write_text("# Guide\nUse **Settings**.\n", encoding="utf-8")
        (self.root / "docs_source_en/coder.md").write_text("# Developer\nPOST /api/example\n", encoding="utf-8")
        (self.root / "docs_source_en/vscode_extension.md").write_text("# Developer\n", encoding="utf-8")
        (self.root / "docs_source_en/webhooks.md").write_text("# Developer\n", encoding="utf-8")
        self.policy = {
            "developer_docs": [
                "docs_source_en/coder.md",
                "docs_source_en/vscode_extension.md",
                "docs_source_en/webhooks.md"
            ],
            "repository_raw_image_prefix": "https://raw.githubusercontent.com/example/docs/main/",
            "forbidden_image_targets": ["docs/demo/rejected.png"],
            "forbidden_patterns": [
                {
                    "name": "raw API endpoint",
                    "pattern": "(?i)\\b(?:GET|POST)\\s+/api/",
                    "help": "customer action only"
                }
            ],
            "pos_preservation": {
                "minimum_image_references": 0,
                "required_text": [],
                "required_images": []
            }
        }
        (self.root / "scripts").mkdir()
        (self.root / "scripts/customer-docs-policy.json").write_text(json.dumps(self.policy), encoding="utf-8")
        (self.root / "docs_source_en/pos.md").write_text("# POS\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_developer_page_is_explicitly_exempt(self):
        self.assertEqual([], MODULE.run(self.root))

    def test_new_page_defaults_to_customer_facing(self):
        path = self.root / "docs_source_en/new_feature.md"
        path.write_text("# Setup\nPOST /api/internal\n", encoding="utf-8")
        findings = MODULE.run(self.root)
        self.assertTrue(any(item.path == path and "raw API endpoint" in item.message for item in findings))

    def test_translated_readme_defaults_to_customer_facing(self):
        path = self.root / "docs/i18n/README_es.md"
        path.parent.mkdir(parents=True)
        path.write_text("# Guía\nPOST /api/internal\n", encoding="utf-8")
        findings = MODULE.run(self.root)
        self.assertTrue(any(item.path == path and "raw API endpoint" in item.message for item in findings))

    def test_missing_local_image_fails(self):
        path = self.root / "docs_source_en/guide.md"
        path.write_text("# Guide\n![Current screen](../images/missing.png)\n", encoding="utf-8")
        findings = MODULE.run(self.root)
        self.assertTrue(any("missing local image" in item.message for item in findings))

    def test_missing_local_html_link_fails(self):
        path = self.root / "docs_source_en/guide.md"
        path.write_text('# Guide\n<a href="missing.html">Missing</a>\n', encoding="utf-8")
        findings = MODULE.run(self.root)
        self.assertTrue(any("broken local HTML link" in item.message for item in findings))

    def test_rejected_image_reference_fails_even_when_file_exists(self):
        rejected = self.root / "docs/demo/rejected.png"
        rejected.parent.mkdir(parents=True)
        rejected.write_bytes(b"not-a-published-screenshot")
        path = self.root / "docs_source_en/guide.md"
        path.write_text(
            "# Guide\n"
            "![Rejected screen](https://raw.githubusercontent.com/example/docs/main/docs/demo/rejected.png)\n",
            encoding="utf-8",
        )
        findings = MODULE.run(self.root)
        self.assertTrue(any("rejected documentation screenshot" in item.message for item in findings))

    def use_repository_forbidden_patterns(self):
        repository_policy = json.loads(
            SCRIPT.with_name("customer-docs-policy.json").read_text(encoding="utf-8")
        )
        self.policy["forbidden_patterns"] = repository_policy["forbidden_patterns"]
        (self.root / "scripts/customer-docs-policy.json").write_text(
            json.dumps(self.policy), encoding="utf-8"
        )

    def test_fixed_plan_entitlements_fail_customer_docs(self):
        self.use_repository_forbidden_patterns()
        path = self.root / "docs_source_en/guide.md"
        path.write_text(
            "# Guide\nAvailable on **Standard+**.\n"
            "| | Free | Standard | Advanced | Enterprise |\n"
            "The free-tier form includes this field.\n",
            encoding="utf-8",
        )
        findings = MODULE.run(self.root)
        plan_findings = [item for item in findings if "fixed plan entitlement" in item.message]
        self.assertEqual(3, len(plan_findings))

    def test_time_sensitive_provider_price_and_revenue_claims_fail(self):
        self.use_repository_forbidden_patterns()
        path = self.root / "docs_source_en/guide.md"
        path.write_text(
            "# Guide\nMessages cost roughly $0.01 at 2026 rates.\n"
            "This typically recovers 5-figure annual revenue.\n",
            encoding="utf-8",
        )
        findings = MODULE.run(self.root)
        messages = [item.message for item in findings]
        self.assertTrue(any("fixed provider price snapshot" in message for message in messages))
        self.assertTrue(any("unsupported revenue claim" in message for message in messages))

    def test_provider_scope_and_baa_roadmap_claim_fail(self):
        self.use_repository_forbidden_patterns()
        path = self.root / "docs_source_en/guide.md"
        path.write_text(
            "# Guide\nApprove `instagram_manage_messages`.\n"
            "A signed BAA with the vendor is on the roadmap.\n",
            encoding="utf-8",
        )
        findings = MODULE.run(self.root)
        messages = [item.message for item in findings]
        self.assertTrue(any("raw provider permission scope" in message for message in messages))
        self.assertTrue(any("unsupported BAA roadmap claim" in message for message in messages))

    def test_internal_release_language_fails_customer_docs(self):
        self.use_repository_forbidden_patterns()
        path = self.root / "docs_source_en/guide.md"
        path.write_text(
            "# Guide\nAcceptance criteria: pass the release gate and CI check.\n",
            encoding="utf-8",
        )
        findings = MODULE.run(self.root)
        release_findings = [item for item in findings if "internal release language" in item.message]
        self.assertEqual(3, len(release_findings))


if __name__ == "__main__":
    unittest.main()
