---
id: RULE-ERROR_HANDLING
owner: Principal Engineer
department: Engineering
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# RULE — Error Handling

> Mandatory engineering standard. Part of the ASFE Engineering Constitution.

---

## 1. Purpose

Establish a reusable, enforceable standard for **Error Handling** across all ASFE SaaS products.

---

## 2. Scope

Applies to: All code.

---

## 3. Out of Scope

Concerns owned by other rules or specialist skills, except where cross-referenced.

---

## 4. Rule Statement

**Errors MUST be handled explicitly, safely, and observably.**

---

## 5. Business Rationale

Reduces risk, improves quality and trust, and lowers long-term cost by making good practice the default.

---

## 6. Technical Rationale

Creates consistent, auditable, automatable behaviour that scales across teams and products.

---

## 7. Industry Standards

- REST
- OpenAPI 3.1
- RFC 9110 (HTTP)
- Twelve-Factor App
- OAuth 2.1
- OIDC
- JSON:API
- RFC 9457 (Problem Details)
- AsyncAPI

---

## 8. Definitions

See the ASFE Glossary (../Knowledge/Glossary.md) for shared terminology.

---

## 9. Applicability

Mandatory for All code. Priority: **High**. Owner: **Principal Engineer**.

---

## 10. Mandatory Requirements (MUST)

- MUST fail safely without leaking internal details.
- MUST return consistent, typed error responses.
- MUST log errors with context and correlation IDs.
- MUST distinguish retryable from terminal errors.

---

## 11. Recommended Practices (SHOULD)

- SHOULD use circuit breakers and backoff for dependencies.
- SHOULD surface actionable user-facing messages.

---

## 12. Optional Enhancements (MAY)

- MAY provide error catalogues with remediation hints.

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

- Swallowing exceptions silently.
- Leaking stack traces to clients.
- Generic 500s with no diagnostics.

---

## 21. Exceptions Process

- Request a time-boxed exception from the Principal Engineer with justification and risk assessment.
- Record exceptions in the risk register with an expiry and remediation plan.
- Security/Privacy/Compliance may veto exceptions.

---

## 22. Review Checklist

- [ ] Does the change satisfy: Fail safely without leaking internal details.
- [ ] Does the change satisfy: Return consistent, typed error responses.
- [ ] Does the change satisfy: Log errors with context and correlation IDs.
- [ ] Does the change satisfy: Distinguish retryable from terminal errors.
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

- REST
- OpenAPI 3.1
- RFC 9110 (HTTP)
- Twelve-Factor App
- OAuth 2.1
- OIDC
- JSON:API
- RFC 9457 (Problem Details)
- AsyncAPI
- ASFE Specification (../ASFE_SPECIFICATION.md)

---

## 29. Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-06-25 | Initial standard. |

---

## 30. Metadata

- **Rule ID:** RULE-ERROR_HANDLING
- **Owner:** Principal Engineer
- **Category:** Engineering
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Effective Date:** 2026-06-25
- **Last Updated:** 2026-06-25
