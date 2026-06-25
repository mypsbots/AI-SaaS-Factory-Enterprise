---
id: KB-AI_ENGINEERING_REFERENCE
framework: AI SaaS Factory Enterprise (ASFE)
owner: Enterprise Architect
department: Knowledge
version: 1.0.0
status: Active
criticality: Medium
review_frequency: Annually
classification: Internal
created: 2026-06-25
updated: 2026-06-25
---

# KNOWLEDGE — AI Engineering Reference

> Reference patterns for building safe, evaluated AI features.

---

## 1. Summary

Reference patterns for building safe, evaluated AI features.

---

## 2. Context

Curated reference knowledge for teams building SaaS products.

---

## 3. Key Concepts

- Model gateway and routing
- Guardrails (input/output/behaviour)
- RAG grounding and citations
- Evaluation and regression gates
- Prompt versioning
- Cost and latency observability

---

## 4. Guidance

- Constrain and validate outputs; never trust raw generations.
- Gate AI changes on automated evaluation.
- Ground answers with access-controlled retrieval and citations.

---

## 5. Pitfalls

- Unbounded prompt injection.
- No evaluation before shipping AI changes.
- Sending sensitive data to models without controls.

---

## 6. Related Documents

- Specification (../ASFE_SPECIFICATION.md)
- Relevant Rules, Skills, and Checklists in this repository.

---

## 7. References

- Official standards and primary sources (see Standards Index).

---

## 8. Metadata

- **Knowledge ID:** KB-AI_ENGINEERING_REFERENCE
- **Owner:** Enterprise Architect
- **Version:** 1.0.0
- **Status:** Active
- **Review Frequency:** Annually
- **Created:** 2026-06-25
- **Updated:** 2026-06-25
