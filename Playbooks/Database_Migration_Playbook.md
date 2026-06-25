---
id: PLAY-DATABASE_MIGRATION_PLAYBOOK
owner: Database Architect
department: Engineering
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# PLAYBOOK — Database Migration Playbook

> Repeatable operational procedure owned by the Database Architect.

---

## 1. Purpose

Provide a consistent, tested procedure for **Database Migration Playbook**.

---

## 2. Objective

Execute schema migrations safely with zero downtime.

---

## 3. Trigger

A schema change is required for a release.

---

## 4. Roles

- Database Architect
- Backend Engineer
- Release Manager

---

## 5. Preconditions

- Required access, tooling, and runbooks are available.
- Stakeholders and communication channels are known.

---

## 6. Procedure

1. Design an expand-then-contract migration.
2. Review and test on production-like data.
3. Back up before applying changes.
4. Apply the expand phase (additive, backward-compatible).
5. Deploy code that supports both schemas.
6. Backfill and verify data integrity.
7. Apply the contract phase after validation.
8. Monitor and keep rollback ready.

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

- ASFE Specification (../ASFE_SPECIFICATION.md)
- Related checklists and runbooks in this repository.

---

## 14. Metadata

- **Playbook ID:** PLAY-DATABASE_MIGRATION_PLAYBOOK
- **Owner:** Database Architect
- **Category:** Engineering
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Created:** 2026-06-25
- **Updated:** 2026-06-25
