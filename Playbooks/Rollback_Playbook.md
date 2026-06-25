---
id: PLAY-ROLLBACK_PLAYBOOK
framework: AI SaaS Factory Enterprise (ASFE)
owner: Release Manager
department: Release
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# PLAYBOOK — Rollback Playbook

> Repeatable operational procedure owned by the Release Manager.

---

## 1. Purpose

Provide a consistent, tested procedure for **Rollback Playbook**.

---

## 2. Objective

Reverse a problematic release quickly and safely.

---

## 3. Trigger

Post-deploy verification fails or a regression is detected.

---

## 4. Roles

- Release Manager
- On-call Engineer
- Incident Commander

---

## 5. Preconditions

- Required access, tooling, and runbooks are available.
- Stakeholders and communication channels are known.

---

## 6. Procedure

1. Decide to roll back using predefined criteria.
2. Halt further rollout immediately.
3. Revert to the last known-good artifact.
4. Reverse or compensate incompatible data migrations.
5. Verify recovery against SLIs and smoke tests.
6. Communicate status and capture the timeline.
7. Open a follow-up to fix forward.

---

## 7. Decision Points

- Escalate when impact or scope exceeds the responder's authority.
- Choose mitigate-forward vs. roll back based on predefined criteria.

---

## 8. Communication Plan

- Notify stakeholders at start, on status changes, and at resolution.
- Use the designated incident/comms channel; keep a timeline.

---

## 9. Rollback / Recovery

- Maintain a tested rollback or recovery path.
- Verify recovery against SLIs and smoke tests.

---

## 10. Post-Procedure Review

- Run a blameless review.
- Log owned, time-bound action items.
- Update this playbook with lessons learned.

---

## 11. Validation Checklist

- [ ] Trigger and roles are clear
- [ ] Each step is actionable and tested
- [ ] Communication plan executed
- [ ] Rollback/recovery verified
- [ ] Post-review completed with actions
- [ ] Metadata complete

---

## 12. Metrics

- Time to execute
- Success rate
- Recurrence rate
- Action-item closure

---

## 13. References

- Specification (../ASFE_SPECIFICATION.md)
- Related checklists and runbooks in this repository.

---

## 14. Metadata

- **Playbook ID:** PLAY-ROLLBACK_PLAYBOOK
- **Owner:** Release Manager
- **Category:** Release
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Created:** 2026-06-25
- **Updated:** 2026-06-25
