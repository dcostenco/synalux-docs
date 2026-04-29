# Accounting & Global Finance Module

![Global Finance Dashboard](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/37_cross_border_finance.png)

The Synalux Accounting & Global Finance module is designed for multi-national healthcare organizations requiring sophisticated hierarchical reporting and multi-currency support.

## Core Features

### Hierarchical Financial Reporting
- **HQ Level:** View consolidated revenue across all international branches.
- **Branch Level:** Isolated financial tracking for regional compliance (US/MD, RO, CA).
- **Service-Level Analysis:** Track profitability by clinical department (ABA, Dental, Pediatrics).

### Multi-Currency & Cross-Border Billing
- **Dynamic Conversion:** Real-time billing in USD, RON, and CAD based on the patient's branch location.
- **Tax Compliance:** Automatic calculation of VAT (Romania) and Sales Tax (CA/US) per jurisdiction.
- **Global Payouts:** Support for international payment gateways with automatic reconciliation.

### Audit & Compliance
- **DDA Approval (Maryland):** Specialized compliance reporting for Maryland Developmental Disabilities Administration.
- **GAAP/IFRS Ready:** Standardized financial exports for external audit and tax preparation.
- **RBAC Financial Locks:** Restrict sensitive financial data to authorized CFO and Management roles only.

## Technical Integration
The module utilizes PostgREST-level RLS policies to ensure that branch-level accountants can only see their specific regional data, while the global CFO has full visibility via the `service_role_unrestricted` policy.
