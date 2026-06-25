---
id: PLAY-ON_CALL_PLAYBOOK
owner: Site Reliability Engineer
department: Operations
version: 1.0.0
status: Active
criticality: High
review_frequency: Quarterly
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# PLAYBOOK — On Call Playbook

> Repeatable operational procedure owned by the Site Reliability Engineer.

---

## 1. Purpose

Provide a consistent, tested procedure for **On Call Playbook**.

---

## 2. Objective

Enable effective, humane on-call coverage.

---

## 3. Trigger

Start of an on-call rotation or a page.

---

## 4. Roles

- On-call Engineer
- Secondary On-call
- Escalation Manager

---

## 5. Preconditions

- Required access, tooling, and runbooks are available.
- Stakeholders and communication channels are known.

---

## 6. Procedure

1. Confirm tooling, access, and runbook availability at handover.
2. Acknowledge pages within the agreed SLA.
3. Triage severity and follow the relevant runbook.
4. Escalate per policy when needed.
5. Mitigate and document actions taken.
6. Hand over open issues with context.
7. Feed recurring toil into automation backlog.

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

- **Playbook ID:** PLAY-ON_CALL_PLAYBOOK
- **Owner:** Site Reliability Engineer
- **Category:** Operations
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Quarterly
- **Created:** 2026-06-25
- **Updated:** 2026-06-25
