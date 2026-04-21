# 🌍 Synalux v11.1 Elite: Global Operations Guide

Welcome to the **Synalux Elite** platform. This guide is designed for Practice Managers, Operations Directors, and Clinical Owners overseeing multi-national behavioral health organizations.

---

## 🚀 The Multi-Branch Advantage
Synalux v11.1 transforms your practice into a unified global enterprise. Manage your US Headquarters, European branches, and Canadian clinics from a single, secure dashboard.

### 🏢 Global Office Management
*   **Centralized Control:** Your main office maintains full oversight of all regional branches (Moldova, Romania, Canada).
*   **Local Privacy:** Each branch operates independently with its own local staff, patient lists, and regional rules, ensuring clinical data remains isolated.
*   **Fast Switching:** Effortlessly switch between different city offices without re-logging.

### 💰 Unified Financial Reporting
*   **Local Currency Billing:** Generate invoices in **USD**, **Moldovan Leu (L)**, **Romanian Leu (lei)**, or **Canadian Dollars** automatically.
*   **Automatic Profit Tracking:** The system monitors global exchange rates to show your total business revenue in your primary currency.
*   **Bookkeeper Ready:** Direct data export for local accounting software used in Europe and North America.

---

## 📝 Smart Clinical Documentation
Synalux uses built-in intelligence to handle the paperwork, so your providers can focus on patients. Managers gain faster sign-offs, while providers maintain 100% legal control.

*   **Private Voice Recording:** Convert session audio into clinical text 100% on the device. No data ever leaves your office, ensuring total patient privacy.
*   **Automatic Treatment Outlines:** The system suggests clinical plans based on proven behavioral methods, completing 80% of the initial writing for your staff.
*   **Smart Billing Codes:** Invoices are automatically calculated based on the actual length and type of session, reducing billing errors and claim denials.

---

## 🛡️ Privacy & Legal Compliance
Synalux Elite is built with a **Pro-Security Core** to keep your global expansion legally safe.

*   **Regional Data Lock:** Patient records in your European branches are stored separately from US records. The main office can review data for quality audits, but individual branches cannot see each other's private information.
*   **Permission-Based Access:** Easily control which staff members can view sensitive health records. You decide who has "Need-to-Know" access based on their job role.
*   **Activity Monitoring:** Every file view or edit is recorded with a permanent time-stamp for legal safety and internal audits.

---

## 📊 Managerial Workflows
### 1. Adding a New Global Branch
To expand into a new country:
1.  Navigate to **Admin > Branches**.
2.  Click **"Add Branch"** and select the country (e.g., Romania).
3.  Set the **Base Currency** and **Practice Type**.
4.  Synalux automatically provisions the localized billing and compliance engine for that region.

### 2. Monitoring Global Revenue
Use the **Consolidated Reporting** dashboard to see:
*   Total unbilled revenue across all global branches (converted to HQ currency).
*   A/R Aging per country.
*   Staff performance metrics by branch.

---

## <details><summary>🛠️ Technical Appendix (For IT/Dev Teams)</summary>

### 🏗️ Elite Architecture & Clinical Logic
*   **On-Device AI (WASM):** Transcription and analysis are executed locally to bypass cloud transit.
*   **O(1) Memory:** Constant-time retrieval of clinical facts using vector embeddings.
*   **Research Intelligence:** Integrated discovery engines (Tavily, PubMed, Semantic Scholar) for clinical grounding.

### 🛡️ Security Specification
*   **Terminal Sandbox:** 11-layer defense for command execution.
*   **SSRF Prevention:** IP pinning and private network blocking for web scrapers.
*   **Data Integrity:** Zod-validated clinical schemas and XSS-safe processing.

### 📁 Technical Documentation
*   **Accounting Interfaces:** [`/docs/ACCOUNTING_INTERFACES.md`](./docs/ACCOUNTING_INTERFACES.md)
*   **Security Model:** See `is_phi_authorized` and `check_workspace_admin_access` in the Database Schema.
*   **API Integration:** REST endpoints for OData (1C) and OAuth 2.0 (Xero/QBO).

</details>

---
**Synalux v11.1 Elite**  
*The Future of Global Behavioral Health Management.*
