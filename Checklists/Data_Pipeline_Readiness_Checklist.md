---
id: CHK-DATA_PIPELINE_READINESS_CHECKLIST
framework: AI SaaS Factory Enterprise (ASFE)
owner: Data Engineer
department: Data
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# CHECKLIST — Data Pipeline Readiness Checklist

> Auditable quality gate. Execute before progressing to the next stage.

---

## 1. Purpose

Validate readiness for **Data Pipeline Readiness Checklist** and prevent defects from reaching production.

---

## 2. Scope

Applies to: New/changed data pipelines.

---

## 3. Out of Scope

Validation owned by other checklists, except where cross-referenced.

---

## 4. When to Use

Use before the relevant quality gate for New/changed data pipelines.

---

## 5. Prerequisites

- Change is complete and self-reviewed.
- Required evidence (tests, scans, evals) is available.

---

## 6. Roles & Responsibilities

- Owner: Data Engineer
- Audience: Data/Eng
- Reviewer: independent peer or specialist

---

## 7. Inputs Required

- The artefact under review
- Relevant rules and standards
- Test/scan/eval evidence

---

## 8. Acceptance Criteria

All items in the Primary Validation Checklist and applicable domain sections pass, with evidence.

---

## 9. Quality Gate

This checklist is the gate for New/changed data pipelines. A failed item blocks progression until resolved or formally excepted.

---

## 10. Pre-Validation Checklist

- [ ] Scope and acceptance criteria confirmed
- [ ] Required reviewers identified
- [ ] Evidence collected and attached

---

## 11. Primary Validation Checklist

- [ ] Pipeline is idempotent and replayable
- [ ] Data-quality tests at ingestion and output
- [ ] Schema changes are backward-compatible
- [ ] Lineage and catalogue updated
- [ ] Monitoring and alerting in place
- [ ] Backfill and recovery procedure defined
- [ ] Sensitive data classified and protected
- [ ] Freshness/SLA targets defined
- [ ] Document/feature follows the framework specification structure
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

## 12. Security Validation

- [ ] AuthN/AuthZ enforced server-side
- [ ] Inputs validated, outputs encoded
- [ ] No secrets in code; secrets manager used
- [ ] SAST/DAST/SCA pass with no open criticals

---

## 13. Privacy Validation

- [ ] Personal data classified and minimised
- [ ] Retention/deletion enforced
- [ ] Data-subject rights supported where applicable

---

## 14. Accessibility Validation

- [ ] Keyboard operable with visible focus
- [ ] Screen-reader compatible
- [ ] Contrast and target sizes meet WCAG 2.2 AA

---

## 15. Performance Validation

- [ ] Performance budgets/SLOs met
- [ ] Tested under realistic load
- [ ] No N+1 or unbounded queries

---

## 16. AI/LLM Validation

- [ ] Model outputs validated and guardrailed
- [ ] AI changes passed evaluation gate
- [ ] No secrets/PII sent to models without controls

---

## 17. Documentation Validation

- [ ] Docs updated and accurate
- [ ] Examples provided where relevant
- [ ] Cross-references valid

---

## 18. Compliance Validation

- [ ] Mapped to applicable controls
- [ ] Audit evidence captured
- [ ] Findings tracked and within SLA

---

## 19. Deployment Readiness

- [ ] Release gates passed
- [ ] Monitoring/alerts in place
- [ ] On-call coverage confirmed

---

## 20. Rollback Readiness

- [ ] Rollback path defined and tested
- [ ] Data migration reversible or compensable
- [ ] Rollback decision criteria documented

---

## 21. Common Failure Patterns

- Skipping items under deadline pressure.
- Treating automated scans as full coverage.
- Missing rollback or recovery validation.

---

## 22. Escalation Process

Unresolved failures escalate to the Data Engineer, then to engineering leadership. Security/Privacy/Compliance failures may block release outright.

---

## 23. Definition of Pass

Every applicable item is checked with evidence and no critical item is failing.

---

## 24. Definition of Fail

Any critical item fails, or evidence is missing for a required item.

---

## 25. Evidence Required

- Test/scan/eval reports
- Reviewer sign-offs
- Relevant dashboards or screenshots

---

## 26. Sign-off Matrix

| Role | Responsibility | Sign-off |
| --- | --- | --- |
| Data Engineer | Owner | [ ] |
| Independent Reviewer | Verification | [ ] |
| Security (if applicable) | Security gate | [ ] |
| Release Manager | Gate decision | [ ] |

---

## 27. Metrics

- Pass rate
- Defect escape rate after gate
- Time to complete checklist

---

## 28. References

- ISO/IEC 11179
- DCAM
- GDPR
- Data Mesh principles
- REST
- OpenAPI 3.1
- RFC 9110 (HTTP)
- Twelve-Factor App
- OAuth 2.1
- OIDC
- OpenTelemetry
- Google SRE (SLO/SLI)
- RED/USE methods
- Specification (../ASFE_SPECIFICATION.md)

---

## 29. Metadata

- **Checklist ID:** CHK-DATA_PIPELINE_READINESS_CHECKLIST
- **Owner:** Data Engineer
- **Category:** Data
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Effective Date:** 2026-06-25
- **Last Updated:** 2026-06-25
