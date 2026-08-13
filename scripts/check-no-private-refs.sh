#!/usr/bin/env bash
# Leak guard for this PUBLIC repository.
#
# Why this exists (2026-08-12): 16 tracked files in this repo referenced the
# PRIVATE repository by name — including a clickable link to a security doc
# inside it, on a customer-facing page, and the private repo's full internal
# directory tree in 11 stale translated READMEs. Nothing checked, so they
# accumulated across releases.
#
# Every other repo in this stack has a guard (prism: check-publish-clean.mjs,
# the private repo: pre-push-audit). This is the one that publishes to the
# world and it had none.
#
# Deliberately NOT matched: `service_role` on its own. It names an RLS policy
# in the documented security model — public by design. A guard that flags
# correct documentation gets disabled, so it stays out.
#
# Usage:  bash scripts/check-no-private-refs.sh
# Exit 0 = clean, 1 = leak found (prints file:line).

set -uo pipefail
cd "$(dirname "$0")/.."

PATTERNS=(
  'synalux-private'                       # the private repo, by name
  'bcba-private'                          # ditto
  'prism-training'                        # private training repo
  'GT Independence'                       # FMS vendor — private commercial relationship
  'Fello FMCS'                            # ditto
  'fusacostenco'                          # personal account
  '[a-zA-Z0-9._%+-]+@gmail\.com'          # personal email of any contributor
  'AIza[0-9A-Za-z_-]{30,}'                # Google API key
  'sk-[A-Za-z0-9]{20,}'                   # OpenAI-style secret
  'sk_live_[A-Za-z0-9]{10,}'              # Stripe live secret
  'eyJhbGciOi[A-Za-z0-9._-]{20,}'         # JWT (Supabase service/anon keys)
  'SUPABASE_SERVICE_ROLE_KEY *[:=] *[^ ]'  # assigned service key
  'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY' # private key material
)

# Adversarial review of the first version of this guard planted seven leak
# variants; it caught NONE. Case was the one that mattered — a heading reading
# "SYNALUX-PRIVATE" or "Synalux-Private" is entirely ordinary prose and slipped
# straight through, in a guard whose only job is to catch that string. Hence -i
# below.
#
# Knowingly still uncaught, recorded rather than left as a silent gap:
#   - separator variants ("synalux private", "synalux_private"). A
#     separator-tolerant pattern would flag legitimate marketing prose such as
#     "Synalux private cloud", and a guard that blocks correct copy gets
#     disabled. Hyphenated is the form that actually appears.
#   - deliberate obfuscation (unicode hyphens, "name (at) gmail.com", a token
#     split across a line break). This guards against accident, not against an
#     author who is trying to evade it.
status=0
for pattern in "${PATTERNS[@]}"; do
  # -I skips binaries (images); -i because case is not a meaningful difference
  # in a leak. Scans tracked files only, so untracked scratch work never fails
  # someone's push.
  if hits=$(git grep -nIiE "$pattern" -- . ':!scripts/check-no-private-refs.sh' 2>/dev/null); then
    if [ -n "$hits" ]; then
      echo "LEAK: pattern /$pattern/ found in this PUBLIC repo:"
      echo "$hits" | sed 's/^/  /'
      status=1
    fi
  fi
done

if [ "$status" -eq 0 ]; then
  echo "leak guard: clean ($(git ls-files | wc -l | tr -d ' ') tracked files scanned)"
else
  echo
  echo "This repository is PUBLIC. Remove the reference, or rephrase it so it"
  echo "does not name private repos, vendors, personal accounts, or secrets."
fi
exit "$status"
