---
id: RULE-FRONTEND_STANDARDS
owner: Frontend Lead
department: Engineering
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# RULE — Frontend Standards

> Mandatory engineering standard. Part of the ASFE Engineering Constitution.

---

## 1. Purpose

Establish a reusable, enforceable standard for **Frontend Standards** across all ASFE SaaS products.

---

## 2. Scope

Applies to: All client applications.

---

## 3. Out of Scope

Concerns owned by other rules or specialist skills, except where cross-referenced.

---

## 4. Rule Statement

**Frontends MUST be accessible, performant, secure, and component-driven.**

---

## 5. Business Rationale

Reduces risk, improves quality and trust, and lowers long-term cost by making good practice the default.

---

## 6. Technical Rationale

Creates consistent, auditable, automatable behaviour that scales across teams and products.

---

## 7. Industry Standards

- WCAG 2.2 AA
- Core Web Vitals
- HTML Living Standard
- ECMAScript
- React
- WAI-ARIA 1.2
- EN 301 549
- Section 508
- RAIL model
- Web Vitals
- OpenTelemetry

---

## 8. Definitions

See the ASFE Glossary (../Knowledge/Glossary.md) for shared terminology.

---

## 9. Applicability

Mandatory for All client applications. Priority: **High**. Owner: **Frontend Lead**.

---

## 10. Mandatory Requirements (MUST)

- MUST use the design system and semantic HTML.
- MUST meet WCAG 2.2 AA and Core Web Vitals budgets.
- MUST sanitise/escape untrusted content (prevent XSS).
- MUST validate API responses defensively.

---

## 11. Recommended Practices (SHOULD)

- SHOULD code-split and lazy-load non-critical paths.
- SHOULD handle all UI states (loading/empty/error).

---

## 12. Optional Enhancements (MAY)

- MAY adopt SSR/edge rendering for performance/SEO.

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

- Div-soup over semantic elements.
- Blocking the main thread.
- Rendering untrusted HTML unsanitised.

---

## 21. Exceptions Process

- Request a time-boxed exception from the Frontend Lead with justification and risk assessment.
- Record exceptions in the risk register with an expiry and remediation plan.
- Security/Privacy/Compliance may veto exceptions.

---

## 22. Review Checklist

- [ ] Does the change satisfy: Use the design system and semantic HTML.
- [ ] Does the change satisfy: Meet WCAG 2.2 AA and Core Web Vitals budgets.
- [ ] Does the change satisfy: Sanitise/escape untrusted content (prevent XSS).
- [ ] Does the change satisfy: Validate API responses defensively.
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

- WCAG 2.2 AA
- Core Web Vitals
- HTML Living Standard
- ECMAScript
- React
- WAI-ARIA 1.2
- EN 301 549
- Section 508
- RAIL model
- Web Vitals
- OpenTelemetry
- ASFE Specification (../ASFE_SPECIFICATION.md)

---

## 29. Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-06-25 | Initial standard. |

---

## 30. Metadata

- **Rule ID:** RULE-FRONTEND_STANDARDS
- **Owner:** Frontend Lead
- **Category:** Engineering
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Effective Date:** 2026-06-25
- **Last Updated:** 2026-06-25
