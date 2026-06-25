---
id: RULE-COMPLIANCE_STANDARDS
owner: Compliance Specialist
department: Compliance
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# RULE — Compliance Standards

> Mandatory engineering standard. Part of the ASFE Engineering Constitution.

---

## 1. Purpose

Establish a reusable, enforceable standard for **Compliance Standards** across all ASFE SaaS products.

---

## 2. Scope

Applies to: All regulated processing.

---

## 3. Out of Scope

Concerns owned by other rules or specialist skills, except where cross-referenced.

---

## 4. Rule Statement

**Operations MUST map to recognised control frameworks with continuous evidence.**

---

## 5. Business Rationale

Reduces risk, improves quality and trust, and lowers long-term cost by making good practice the default.

---

## 6. Technical Rationale

Creates consistent, auditable, automatable behaviour that scales across teams and products.

---

## 7. Industry Standards

- SOC 2 Type II
- ISO/IEC 27001
- GDPR
- PCI DSS 4.0
- OWASP ASVS
- OWASP Top 10
- OWASP API Security Top 10
- NIST CSF
- NIST SP 800-53
- CIS Controls
- CCPA/CPRA
- ISO/IEC 27701
- NIST Privacy Framework

---

## 8. Definitions

See the ASFE Glossary (../Knowledge/Glossary.md) for shared terminology.

---

## 9. Applicability

Mandatory for All regulated processing. Priority: **High**. Owner: **Compliance Specialist**.

---

## 10. Mandatory Requirements (MUST)

- MUST map controls to SOC 2 / ISO 27001 / GDPR / PCI as applicable.
- MUST assign an owner and test to each control.
- MUST collect audit evidence continuously.
- MUST track and close findings within SLA.

---

## 11. Recommended Practices (SHOULD)

- SHOULD automate evidence collection.
- SHOULD maintain a current risk register.

---

## 12. Optional Enhancements (MAY)

- MAY pursue additional certifications as needed.

---

## 13. Architecture Guidance

- Prefer declarative, reproducible, automated implementations.
- Design for least privilege, failure, and recovery.

---

## 14. Security Requirements

- Enforce zero trust and least privilege.
- Validate inputs, encode outputs, manage secrets centrally.

---

## 15. Privacy Requirements

- Minimise personal data and honour data-subject rights.
- Apply retention limits and secure deletion.

---

## 16. Accessibility Requirements

- Any user-facing output must meet WCAG 2.2 AA.

---

## 17. Performance Requirements

- Respect performance budgets and SLOs; avoid unbounded work.

---

## 18. AI/LLM Considerations

- Validate model outputs; never send secrets/PII to models without controls.
- Gate AI changes on automated evaluation.

---

## 19. Implementation Examples

Apply the MUST requirements via automated checks in CI and code/design review. Document any approved exceptions (section 21).

---

## 20. Common Anti-patterns

- Annual audit-cramming.
- Policies without enforcement.
- Unowned, ageing findings.

---

## 21. Exceptions Process

- Request a time-boxed exception from the Compliance Specialist with justification and risk assessment.
- Record exceptions in the risk register with an expiry and remediation plan.
- Security/Privacy/Compliance may veto exceptions.

---

## 22. Review Checklist

- [ ] Does the change satisfy: Map controls to SOC 2 / ISO 27001 / GDPR / PCI as applicable.
- [ ] Does the change satisfy: Assign an owner and test to each control.
- [ ] Does the change satisfy: Collect audit evidence continuously.
- [ ] Does the change satisfy: Track and close findings within SLA.
- [ ] Are responsibilities and scope unambiguous?
- [ ] Are security implications identified and addressed?
- [ ] Is personal data handled lawfully and minimally?
- [ ] Are accessibility requirements (WCAG 2.2 AA) considered?
- [ ] Are performance budgets and SLOs respected?
- [ ] Is observability (logs, metrics, traces) in place?
- [ ] Are errors handled explicitly and safely?
- [ ] Is backward compatibility preserved or deprecation planned?
- [ ] Are tests present and meaningful for the change?
- [ ] Are dependencies pinned, scanned, and current?
- [ ] Are secrets managed centrally and never committed?
- [ ] Is least-privilege access enforced?
- [ ] Is documentation updated and accurate?
- [ ] Are relevant industry standards applied?
- [ ] Are collaboration and review owners identified?
- [ ] Is there a tested rollback or recovery path?
- [ ] Are KPIs/metrics defined to measure success?
- [ ] Are anti-patterns explicitly avoided?
- [ ] Is the change reproducible and automated where possible?
- [ ] Has a peer or specialist reviewer approved the work?

---

## 23. Validation Checklist

- [ ] Document/feature follows the ASFE specification structure
- [ ] Metadata (YAML front matter) is complete and accurate
- [ ] Purpose and scope are clearly stated
- [ ] Security considerations are documented and addressed
- [ ] Privacy and data-handling requirements are met
- [ ] Accessibility requirements (WCAG 2.2 AA) are addressed
- [ ] Performance budgets and targets are defined
- [ ] Observability and telemetry are in place
- [ ] Error handling is explicit and safe
- [ ] Inputs are validated and outputs encoded
- [ ] Authentication and authorization are enforced server-side
- [ ] Secrets are stored in a secrets manager (none in code)
- [ ] Dependencies are pinned, scanned, and patched
- [ ] Automated tests cover new/changed behaviour
- [ ] CI quality gates pass (lint, test, scan)
- [ ] Backward compatibility is preserved or deprecation is planned
- [ ] Rollback or recovery path is defined and tested
- [ ] Relevant industry standards are referenced and applied
- [ ] Collaboration matrix and reviewers are identified
- [ ] KPIs and success metrics are defined
- [ ] Anti-patterns are explicitly avoided
- [ ] Documentation is updated and renders correctly
- [ ] Cross-references to related documents are valid
- [ ] Acceptance criteria are objectively verifiable
- [ ] Change is reproducible and automated where feasible
- [ ] Audit/evidence requirements are satisfied
- [ ] Capacity and cost implications are assessed
- [ ] Internationalisation and localisation are considered where relevant
- [ ] Risk register/exceptions updated where applicable
- [ ] Definition of Done is fully satisfied

---

## 24. Definition of Compliance

Compliant only if ALL mandatory (MUST) requirements are met and verified, with evidence, and no unexpired exceptions remain unaddressed.

---

## 25. Non-compliance Risks

- Security, privacy, or reliability incidents.
- Audit findings and certification risk.
- Increased defect and maintenance cost.

---

## 26. Monitoring & Enforcement

- Enforced via automated CI gates and code/design review.
- Violations tracked as defects with remediation SLAs.

---

## 27. Metrics & KPIs

- Compliance rate
- Exception count and age
- Related incident/defect rate

---

## 28. References

- SOC 2 Type II
- ISO/IEC 27001
- GDPR
- PCI DSS 4.0
- OWASP ASVS
- OWASP Top 10
- OWASP API Security Top 10
- NIST CSF
- NIST SP 800-53
- CIS Controls
- CCPA/CPRA
- ISO/IEC 27701
- NIST Privacy Framework
- ASFE Specification (../ASFE_SPECIFICATION.md)

---

## 29. Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-06-25 | Initial standard. |

---

## 30. Metadata

- **Rule ID:** RULE-COMPLIANCE_STANDARDS
- **Owner:** Compliance Specialist
- **Category:** Compliance
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Effective Date:** 2026-06-25
- **Last Updated:** 2026-06-25
