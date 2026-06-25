#!/usr/bin/env python3
"""ASFE Documentation-as-Code generator.

Generates every ASFE Markdown document (skills, rules, checklists, playbooks,
templates, knowledge, department indexes, root README and specification) from
the data tables, applying the exact section schemas defined in the master
generator prompts. Run from the repository root:

    python3 _build/generate_asfe.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from asfe_common import (  # noqa: E402
    VERSION, TODAY, CROSS_CUTTING_PRINCIPLES, DEPARTMENTS,
    FRAMEWORK_NAME, FRAMEWORK_ABBR, FRAMEWORK_FULL,
    front_matter, h, bullets, numbered, checkboxes, hr, standards_for, slugify_id,
)
from asfe_data_skills import SKILLS  # noqa: E402
from asfe_data_docs import RULES, CHECKLISTS, PLAYBOOKS, TEMPLATES, KNOWLEDGE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPT_BY_CODE = {code: (title, desc) for code, title, desc in DEPARTMENTS}
WRITTEN = []

# ---------------------------------------------------------------------------
# Asset -> department mapping (drives the per-department "Related Assets" links).
# An asset belongs to a department if its owning role maps to that department,
# or any of its domain tags map to that department. This gives precise,
# discoverable cross-references instead of bare folder links.
# ---------------------------------------------------------------------------
ROLE_TO_DEPT = {
    "API Architect": "10_API",
    "Principal Engineer": "05_Backend",
    "Security Architect": "14_Security",
    "Security Engineer": "14_Security",
    "Privacy Engineer": "15_Privacy",
    "Observability Engineer": "19_Observability",
    "QA Lead": "17_QA",
    "Engineering Manager": "12_DevOps",
    "DevOps Engineer": "12_DevOps",
    "Cloud Architect": "11_Cloud",
    "Database Architect": "09_Database",
    "Accessibility Specialist": "17_QA",
    "Performance Engineer": "18_Performance",
    "AI Engineering Director": "06_AI",
    "Prompt Engineer": "06_AI",
    "RAG Engineer": "07_RAG",
    "DevSecOps Engineer": "13_DevSecOps",
    "Technical Writer": "02_Product",
    "Release Manager": "26_Release",
    "Site Reliability Engineer": "27_Operations",
    "Compliance Specialist": "16_Compliance",
    "Frontend Lead": "04_Frontend",
    "Enterprise Architect": "00_Governance",
    "SEO/AEO/GEO Specialist": "20_SEO",
    "Payments Engineer": "24_Finance",
    "Product Manager": "02_Product",
    "Customer Success": "23_CustomerSuccess",
}

TAG_TO_DEPTS = {
    "backend": ["05_Backend"],
    "frontend": ["04_Frontend"],
    "api": ["10_API"],
    "security": ["14_Security"],
    "privacy": ["15_Privacy", "25_Legal"],
    "compliance": ["16_Compliance", "25_Legal"],
    "ai": ["06_AI"],
    "eval": ["06_AI"],
    "data": ["08_Data"],
    "cloud": ["11_Cloud"],
    "observability": ["19_Observability"],
    "quality": ["17_QA"],
    "performance": ["18_Performance"],
    "accessibility": ["17_QA", "04_Frontend", "03_UX"],
    "growth": ["20_SEO", "21_Marketing"],
    "release": ["26_Release"],
    "finance": ["24_Finance"],
    "general": [],
}

# Templates relevant to specific departments (templates are otherwise general).
TEMPLATE_MAP = {
    "00_Governance": ["SKILLS_Template", "RULES_Template", "CHECKLIST_Template",
                      "PLAYBOOK_Template", "KNOWLEDGE_Template", "ADR_Template"],
    "01_Executive": ["PRD_Template"],
    "02_Product": ["PRD_Template", "RFC_Template"],
    "03_UX": ["PRD_Template"],
    "04_Frontend": ["ADR_Template", "RFC_Template"],
    "05_Backend": ["ADR_Template", "RFC_Template", "Runbook_Template"],
    "06_AI": ["RFC_Template", "ADR_Template"],
    "07_RAG": ["RFC_Template"],
    "08_Data": ["ADR_Template"],
    "09_Database": ["ADR_Template", "Runbook_Template"],
    "10_API": ["ADR_Template", "RFC_Template"],
    "11_Cloud": ["ADR_Template", "RFC_Template", "Runbook_Template"],
    "12_DevOps": ["Runbook_Template", "ADR_Template"],
    "13_DevSecOps": ["RFC_Template"],
    "14_Security": ["Postmortem_Template", "RFC_Template"],
    "15_Privacy": ["Postmortem_Template"],
    "17_QA": ["CHECKLIST_Template"],
    "19_Observability": ["Runbook_Template"],
    "26_Release": ["Runbook_Template"],
    "27_Operations": ["Runbook_Template", "Postmortem_Template"],
}

# Foundational knowledge linked from every department; domain knowledge added per department.
FOUNDATIONAL_KNOWLEDGE = ["Engineering_Principles", "Standards_Index", "Glossary", "Technology_Radar"]
KNOWLEDGE_DOMAIN_MAP = {
    "11_Cloud": ["Security_Reference_Architecture"],
    "13_DevSecOps": ["Security_Reference_Architecture"],
    "14_Security": ["Security_Reference_Architecture"],
    "16_Compliance": ["Security_Reference_Architecture"],
    "06_AI": ["AI_Engineering_Reference"],
    "07_RAG": ["AI_Engineering_Reference"],
}


def asset_departments(owner: str, tags) -> set:
    depts = set()
    if owner in ROLE_TO_DEPT:
        depts.add(ROLE_TO_DEPT[owner])
    for tag in tags:
        depts.update(TAG_TO_DEPTS.get(tag, []))
    return depts


def assets_for_department(code: str) -> dict:
    """Return the rules, checklists, playbooks, templates and knowledge linked to
    a department, de-duplicated and sorted for stable, readable output."""
    rules = sorted([r for r in RULES if code in asset_departments(r["owner"], r["tags"])],
                   key=lambda x: x["name"])
    checklists = sorted([c for c in CHECKLISTS if code in asset_departments(c["owner"], c["tags"])],
                        key=lambda x: x["name"])
    playbooks = sorted([p for p in PLAYBOOKS if code in asset_departments(p["owner"], p["tags"])],
                       key=lambda x: x["name"])
    template_names = TEMPLATE_MAP.get(code, [])
    templates = [t for t in TEMPLATES if t["name"] in template_names]
    knowledge_names = FOUNDATIONAL_KNOWLEDGE + KNOWLEDGE_DOMAIN_MAP.get(code, [])
    knowledge = [k for nm in knowledge_names for k in KNOWLEDGE if k["name"] == nm]
    return {"rules": rules, "checklists": checklists, "playbooks": playbooks,
            "templates": templates, "knowledge": knowledge}


def write(path: str, content: str) -> None:
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    WRITTEN.append(path)


def humanize(name: str) -> str:
    return name.replace("_", " ").replace("/", " / ")


def join_doc(parts: list) -> str:
    """Assemble a document: front matter first, then blocks separated by blank
    lines, with a horizontal rule placed only *before* each top-level (## ) and
    H1 heading section for clean visual separation. Avoids the broken
    double-delimiter that occurs when joining the YAML block with a rule."""
    out = [parts[0]]  # YAML front matter
    for block in parts[1:]:
        stripped = block.lstrip()
        if stripped.startswith("## "):
            out.append("\n---\n")
        out.append(block)
    text = "\n\n".join(out)
    # Collapse the artefact of inserting a standalone divider block.
    return text.replace("\n\n\n---\n\n\n", "\n\n---\n\n")


# Universal review questions reused across documents (ensures >=20 with domain items).
UNIVERSAL_REVIEW = [
    "Are responsibilities and scope unambiguous?",
    "Are security implications identified and addressed?",
    "Is personal data handled lawfully and minimally?",
    "Are accessibility requirements (WCAG 2.2 AA) considered?",
    "Are performance budgets and SLOs respected?",
    "Is observability (logs, metrics, traces) in place?",
    "Are errors handled explicitly and safely?",
    "Is backward compatibility preserved or deprecation planned?",
    "Are tests present and meaningful for the change?",
    "Are dependencies pinned, scanned, and current?",
    "Are secrets managed centrally and never committed?",
    "Is least-privilege access enforced?",
    "Is documentation updated and accurate?",
    "Are relevant industry standards applied?",
    "Are collaboration and review owners identified?",
    "Is there a tested rollback or recovery path?",
    "Are KPIs/metrics defined to measure success?",
    "Are anti-patterns explicitly avoided?",
    "Is the change reproducible and automated where possible?",
    "Has a peer or specialist reviewer approved the work?",
]

UNIVERSAL_VALIDATION = [
    "Document/feature follows the framework specification structure",
    "Metadata (YAML front matter) is complete and accurate",
    "Purpose and scope are clearly stated",
    "Security considerations are documented and addressed",
    "Privacy and data-handling requirements are met",
    "Accessibility requirements (WCAG 2.2 AA) are addressed",
    "Performance budgets and targets are defined",
    "Observability and telemetry are in place",
    "Error handling is explicit and safe",
    "Inputs are validated and outputs encoded",
    "Authentication and authorization are enforced server-side",
    "Secrets are stored in a secrets manager (none in code)",
    "Dependencies are pinned, scanned, and patched",
    "Automated tests cover new/changed behaviour",
    "CI quality gates pass (lint, test, scan)",
    "Backward compatibility is preserved or deprecation is planned",
    "Rollback or recovery path is defined and tested",
    "Relevant industry standards are referenced and applied",
    "Collaboration matrix and reviewers are identified",
    "KPIs and success metrics are defined",
    "Anti-patterns are explicitly avoided",
    "Documentation is updated and renders correctly",
    "Cross-references to related documents are valid",
    "Acceptance criteria are objectively verifiable",
    "Change is reproducible and automated where feasible",
    "Audit/evidence requirements are satisfied",
    "Capacity and cost implications are assessed",
    "Internationalisation and localisation are considered where relevant",
    "Risk register/exceptions updated where applicable",
    "Definition of Done is fully satisfied",
]


def metadata_block(doc_id, owner, dept, criticality, status="Active", review="Quarterly"):
    return front_matter({
        "id": doc_id,
        "framework": FRAMEWORK_FULL,
        "owner": owner,
        "department": dept,
        "version": VERSION,
        "status": status,
        "criticality": criticality,
        "review_frequency": review,
        "classification": "Internal",
        "created": TODAY,
        "updated": TODAY,
    })


# ---------------------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------------------
def gen_skill(s: dict) -> str:
    title = humanize(s["name"])
    dept_title = DEPT_BY_CODE.get(s["dept"], (s["dept"], ""))[0]
    stds = standards_for(*s["tags"])
    doc_id = slugify_id("SKILL", s["name"])
    collaborators = s["collaborators"]
    parts = []
    parts.append(metadata_block(doc_id, s["name"].replace("_", " "), dept_title, s["criticality"]))
    parts.append(h(1, f"SKILL — {title}"))
    parts.append(f"> Specialist engineering handbook for the **{title}** role. Reusable across any SaaS product.")

    parts.append(h(2, "1. Purpose"))
    parts.append(f"Define the responsibilities, authority, standards, and quality expectations for the {title} so that AI assistants and human engineers deliver consistent, production-grade outcomes.")

    parts.append(h(2, "2. Mission"))
    parts.append(s["mission"])

    parts.append(h(2, "3. Vision"))
    parts.append(f"A {title} function that is secure-by-default, measurable, automated, and continuously improving across every SaaS product you build.")

    parts.append(h(2, "4. Role Overview"))
    parts.append(f"The {title} operates in the **{dept_title}** department, reports to the **{s['reports_to']}**, and collaborates closely with {', '.join(collaborators)}.")

    parts.append(h(2, "5. Responsibilities"))
    parts.append(bullets(s["responsibilities"]))

    parts.append(h(2, "6. Scope"))
    parts.append(bullets(s["scope"]))

    parts.append(h(2, "7. Out of Scope"))
    parts.append(bullets(s["out_of_scope"]))

    parts.append(h(2, "8. Primary Objectives"))
    parts.append(bullets(s["primary"]))

    parts.append(h(2, "9. Secondary Objectives"))
    parts.append(bullets([
        "Reduce toil through automation and reusable assets.",
        "Mentor peers and share domain knowledge.",
        "Continuously improve quality and reliability metrics.",
    ]))

    parts.append(h(2, "10. Expected Deliverables"))
    parts.append(bullets(s["deliverables"]))

    parts.append(h(2, "11. Inputs"))
    parts.append(bullets([
        "Approved requirements and acceptance criteria",
        "Relevant rules, checklists, and templates",
        "Upstream contracts, designs, and data",
    ]))

    parts.append(h(2, "12. Outputs"))
    parts.append(bullets(s["deliverables"]))

    parts.append(h(2, "13. Required Knowledge"))
    parts.append(bullets([
        f"Deep domain expertise relevant to {dept_title}",
        "The framework specification, rules, and quality gates",
        "Applicable industry standards (see section 20)",
    ]))

    parts.append(h(2, "14. Required Technical Skills"))
    parts.append(bullets([
        "Designing, building, and operating production systems in the domain",
        "Testing, observability, and secure engineering practices",
        "Automation and Documentation-as-Code",
    ]))

    parts.append(h(2, "15. Required Soft Skills"))
    parts.append(bullets([
        "Clear written and verbal communication",
        "Collaboration and constructive review",
        "Pragmatic prioritisation and ownership",
    ]))

    parts.append(h(2, "16. Decision Authority"))
    parts.append(bullets([
        f"Owns decisions within {dept_title} scope as defined above.",
        f"Escalates cross-cutting decisions to the {s['reports_to']}.",
        "Cannot override Security, Privacy, or Compliance vetoes.",
    ]))

    parts.append(h(2, "17. Engineering Principles"))
    parts.append(bullets(CROSS_CUTTING_PRINCIPLES))

    parts.append(h(2, "18. Architecture Principles"))
    parts.append(bullets([
        "Favour simple, well-bounded, testable designs.",
        "Design for failure, observability, and recovery.",
        "Prefer reproducible, automated, declarative approaches.",
    ]))

    parts.append(h(2, "19. Industry Standards"))
    parts.append(bullets(stds))

    parts.append(h(2, "20. Best Practices"))
    parts.append(bullets(s["best_practices"]))

    parts.append(h(2, "21. Anti-patterns"))
    parts.append(bullets(s["anti_patterns"]))

    parts.append(h(2, "22. Security Considerations"))
    parts.append(bullets([
        "Apply zero trust and least privilege to all access.",
        "Validate inputs, encode outputs, and avoid injection.",
        "Keep secrets in a secrets manager; never in code.",
        "Ensure security findings are tracked and remediated.",
    ]))

    parts.append(h(2, "23. Performance Considerations"))
    parts.append(bullets([
        "Respect performance budgets and SLOs.",
        "Measure before optimising; watch tail latency.",
        "Plan capacity with cost awareness.",
    ]))

    parts.append(h(2, "24. Accessibility Considerations"))
    parts.append(bullets([
        "Support WCAG 2.2 AA for any user-facing output.",
        "Ensure keyboard operability and assistive-tech support.",
        "Provide text alternatives and sufficient contrast.",
    ]))

    parts.append(h(2, "25. Privacy Considerations"))
    parts.append(bullets([
        "Minimise personal data; justify each field.",
        "Support data-subject rights and retention limits.",
        "Never log or expose unmasked personal data.",
    ]))

    parts.append(h(2, "26. Compliance Considerations"))
    parts.append(bullets([
        "Map work to applicable controls (SOC 2, ISO 27001, GDPR).",
        "Produce auditable evidence for controls.",
        "Track and close compliance findings within SLA.",
    ]))

    parts.append(h(2, "27. Quality Gates"))
    parts.append(bullets([
        f"Approves work within {dept_title} scope when standards and checklists pass.",
        "Rejects work that fails security, privacy, accessibility, or quality gates.",
        "Requires automated evidence (tests, scans, evals) before sign-off.",
    ]))

    parts.append(h(2, "28. Collaboration Matrix"))
    parts.append("\n".join([
        "| Interaction | Roles |",
        "| --- | --- |",
        f"| Must Consult | {', '.join(collaborators[:3])} |",
        f"| Must Inform | {s['reports_to']}, Release Manager |",
        f"| Can Approve | Work within {dept_title} scope |",
        f"| Can Reject | Changes violating {dept_title} standards or gates |",
        f"| Escalation Path | {s['reports_to']} → Engineering Leadership |",
    ]))

    parts.append(h(2, "29. Review Checklist"))
    domain_review = [f"Are {dept_title}-specific best practices applied?",
                     f"Have {dept_title} anti-patterns been avoided?",
                     f"Are {dept_title} deliverables complete and reviewed?"]
    parts.append(checkboxes(domain_review + UNIVERSAL_REVIEW))

    parts.append(h(2, "30. Definition of Done"))
    parts.append(bullets([
        "All responsibilities for the change are fulfilled.",
        "All required quality gates pass with evidence.",
        "Documentation and metadata are complete.",
        "Validation checklist (section 33) is satisfied.",
    ]))

    parts.append(h(2, "31. KPIs"))
    parts.append(bullets(s["kpis"]))

    parts.append(h(2, "32. Success Metrics"))
    parts.append(bullets([
        "Sustained achievement of the KPIs above.",
        "Low defect-escape and incident-recurrence rates.",
        "High reuse of the role's standardised outputs.",
    ]))

    parts.append(h(2, "33. Deliverable Templates"))
    parts.append(bullets([
        "Use the shared document templates (see ../Templates/) for all outputs.",
        "Attach evidence (tests, scans, evals) to deliverables.",
    ]))

    parts.append(h(2, "34. AI Prompting Guidance"))
    parts.append(bullets([
        f"AI assistants should adopt the {title} persona and authority defined here.",
        "Enforce the principles, standards, and checklists in every response.",
        "Never exceed the role's decision authority; escalate instead.",
        "Produce auditable, standards-aligned outputs with citations.",
    ]))

    parts.append(h(2, "35. Validation Checklist"))
    parts.append(checkboxes(UNIVERSAL_VALIDATION))

    parts.append(h(2, "36. Continuous Improvement"))
    parts.append(bullets([
        "Review metrics and incidents to find improvements.",
        "Track evolving standards and update this skill.",
        "Share learnings into the shared knowledge base.",
    ]))

    parts.append(h(2, "37. References"))
    parts.append(bullets([f"{x} (official standard/specification)" for x in stds] +
                         ["Specification (../ASFE_SPECIFICATION.md)"]))

    parts.append(h(2, "38. Version History"))
    parts.append("\n".join([
        "| Version | Date | Change |",
        "| --- | --- | --- |",
        f"| {VERSION} | {TODAY} | Initial enterprise skill definition. |",
    ]))

    parts.append(h(2, "39. Metadata"))
    parts.append("\n".join([
        f"- **Owner:** {s['name'].replace('_', ' ')}",
        f"- **Department:** {dept_title}",
        f"- **Version:** {VERSION}",
        "- **Status:** Active",
        "- **Review Frequency:** Quarterly",
        f"- **Criticality:** {s['criticality']}",
        f"- **Created:** {TODAY}",
        f"- **Updated:** {TODAY}",
    ]))

    return join_doc(parts)


# ---------------------------------------------------------------------------
# RULES
# ---------------------------------------------------------------------------
def gen_rule(r: dict) -> str:
    title = humanize(r["name"])
    stds = standards_for(*r["tags"])
    doc_id = slugify_id("RULE", r["name"])
    parts = []
    parts.append(metadata_block(doc_id, r["owner"], r["category"], r["priority"]))
    parts.append(h(1, f"RULE — {title}"))
    parts.append(f"> Mandatory engineering standard. Reusable across any SaaS product.")

    parts.append(h(2, "1. Purpose"))
    parts.append(f"Establish a reusable, enforceable standard for **{title}** across all SaaS products.")
    parts.append(h(2, "2. Scope"))
    parts.append(f"Applies to: {r['applies_to']}.")
    parts.append(h(2, "3. Out of Scope"))
    parts.append("Concerns owned by other rules or specialist skills, except where cross-referenced.")
    parts.append(h(2, "4. Rule Statement"))
    parts.append(f"**{r['statement']}**")
    parts.append(h(2, "5. Business Rationale"))
    parts.append("Reduces risk, improves quality and trust, and lowers long-term cost by making good practice the default.")
    parts.append(h(2, "6. Technical Rationale"))
    parts.append("Creates consistent, auditable, automatable behaviour that scales across teams and products.")
    parts.append(h(2, "7. Industry Standards"))
    parts.append(bullets(stds))
    parts.append(h(2, "8. Definitions"))
    parts.append("See the Glossary (../Knowledge/Glossary.md) for shared terminology.")
    parts.append(h(2, "9. Applicability"))
    parts.append(f"Mandatory for {r['applies_to']}. Priority: **{r['priority']}**. Owner: **{r['owner']}**.")
    parts.append(h(2, "10. Mandatory Requirements (MUST)"))
    parts.append(bullets([f"MUST {m[0].lower() + m[1:]}" for m in r["musts"]]))
    parts.append(h(2, "11. Recommended Practices (SHOULD)"))
    parts.append(bullets([f"SHOULD {x[0].lower() + x[1:]}" for x in r["shoulds"]]))
    parts.append(h(2, "12. Optional Enhancements (MAY)"))
    parts.append(bullets([f"MAY {x[0].lower() + x[1:]}" for x in r["mays"]]))
    parts.append(h(2, "13. Architecture Guidance"))
    parts.append(bullets(["Prefer declarative, reproducible, automated implementations.",
                          "Design for least privilege, failure, and recovery."]))
    parts.append(h(2, "14. Security Requirements"))
    parts.append(bullets(["Enforce zero trust and least privilege.",
                          "Validate inputs, encode outputs, manage secrets centrally."]))
    parts.append(h(2, "15. Privacy Requirements"))
    parts.append(bullets(["Minimise personal data and honour data-subject rights.",
                          "Apply retention limits and secure deletion."]))
    parts.append(h(2, "16. Accessibility Requirements"))
    parts.append(bullets(["Any user-facing output must meet WCAG 2.2 AA."]))
    parts.append(h(2, "17. Performance Requirements"))
    parts.append(bullets(["Respect performance budgets and SLOs; avoid unbounded work."]))
    parts.append(h(2, "18. AI/LLM Considerations"))
    parts.append(bullets(["Validate model outputs; never send secrets/PII to models without controls.",
                          "Gate AI changes on automated evaluation."]))
    parts.append(h(2, "19. Implementation Examples"))
    parts.append("Apply the MUST requirements via automated checks in CI and code/design review. Document any approved exceptions (section 21).")
    parts.append(h(2, "20. Common Anti-patterns"))
    parts.append(bullets(r["anti"]))
    parts.append(h(2, "21. Exceptions Process"))
    parts.append(bullets([f"Request a time-boxed exception from the {r['owner']} with justification and risk assessment.",
                          "Record exceptions in the risk register with an expiry and remediation plan.",
                          "Security/Privacy/Compliance may veto exceptions."]))
    parts.append(h(2, "22. Review Checklist"))
    parts.append(checkboxes([f"Does the change satisfy: {m}" for m in r["musts"]] + UNIVERSAL_REVIEW))
    parts.append(h(2, "23. Validation Checklist"))
    parts.append(checkboxes(UNIVERSAL_VALIDATION))
    parts.append(h(2, "24. Definition of Compliance"))
    parts.append("Compliant only if ALL mandatory (MUST) requirements are met and verified, with evidence, and no unexpired exceptions remain unaddressed.")
    parts.append(h(2, "25. Non-compliance Risks"))
    parts.append(bullets(["Security, privacy, or reliability incidents.",
                          "Audit findings and certification risk.",
                          "Increased defect and maintenance cost."]))
    parts.append(h(2, "26. Monitoring & Enforcement"))
    parts.append(bullets(["Enforced via automated CI gates and code/design review.",
                          "Violations tracked as defects with remediation SLAs."]))
    parts.append(h(2, "27. Metrics & KPIs"))
    parts.append(bullets(["Compliance rate", "Exception count and age", "Related incident/defect rate"]))
    parts.append(h(2, "28. References"))
    parts.append(bullets([f"{x}" for x in stds] + ["Specification (../ASFE_SPECIFICATION.md)"]))
    parts.append(h(2, "29. Version History"))
    parts.append("\n".join(["| Version | Date | Change |", "| --- | --- | --- |",
                            f"| {VERSION} | {TODAY} | Initial standard. |"]))
    parts.append(h(2, "30. Metadata"))
    parts.append("\n".join([f"- **Rule ID:** {doc_id}", f"- **Owner:** {r['owner']}",
                            f"- **Category:** {r['category']}", f"- **Version:** {VERSION}",
                            "- **Status:** Active", "- **Review Frequency:** Quarterly",
                            f"- **Effective Date:** {TODAY}", f"- **Last Updated:** {TODAY}"]))
    return join_doc(parts)


# ---------------------------------------------------------------------------
# CHECKLISTS
# ---------------------------------------------------------------------------
def gen_checklist(c: dict) -> str:
    title = humanize(c["name"])
    stds = standards_for(*c["tags"])
    doc_id = slugify_id("CHK", c["name"])
    parts = []
    parts.append(metadata_block(doc_id, c["owner"], c["category"], c["priority"]))
    parts.append(h(1, f"CHECKLIST — {title}"))
    parts.append(f"> Auditable quality gate. Execute before progressing to the next stage.")
    parts.append(h(2, "1. Purpose"))
    parts.append(f"Validate readiness for **{title}** and prevent defects from reaching production.")
    parts.append(h(2, "2. Scope"))
    parts.append(f"Applies to: {c['applies_to']}.")
    parts.append(h(2, "3. Out of Scope"))
    parts.append("Validation owned by other checklists, except where cross-referenced.")
    parts.append(h(2, "4. When to Use"))
    parts.append(f"Use before the relevant quality gate for {c['applies_to']}.")
    parts.append(h(2, "5. Prerequisites"))
    parts.append(bullets(["Change is complete and self-reviewed.",
                          "Required evidence (tests, scans, evals) is available."]))
    parts.append(h(2, "6. Roles & Responsibilities"))
    parts.append(bullets([f"Owner: {c['owner']}", f"Audience: {c['audience']}",
                          "Reviewer: independent peer or specialist"]))
    parts.append(h(2, "7. Inputs Required"))
    parts.append(bullets(["The artefact under review", "Relevant rules and standards", "Test/scan/eval evidence"]))
    parts.append(h(2, "8. Acceptance Criteria"))
    parts.append("All items in the Primary Validation Checklist and applicable domain sections pass, with evidence.")
    parts.append(h(2, "9. Quality Gate"))
    parts.append(f"This checklist is the gate for {c['applies_to']}. A failed item blocks progression until resolved or formally excepted.")
    parts.append(h(2, "10. Pre-Validation Checklist"))
    parts.append(checkboxes(["Scope and acceptance criteria confirmed",
                            "Required reviewers identified",
                            "Evidence collected and attached"]))
    parts.append(h(2, "11. Primary Validation Checklist"))
    parts.append(checkboxes(c["primary"] + UNIVERSAL_VALIDATION))
    parts.append(h(2, "12. Security Validation"))
    parts.append(checkboxes(["AuthN/AuthZ enforced server-side", "Inputs validated, outputs encoded",
                            "No secrets in code; secrets manager used", "SAST/DAST/SCA pass with no open criticals"]))
    parts.append(h(2, "13. Privacy Validation"))
    parts.append(checkboxes(["Personal data classified and minimised", "Retention/deletion enforced",
                            "Data-subject rights supported where applicable"]))
    parts.append(h(2, "14. Accessibility Validation"))
    parts.append(checkboxes(["Keyboard operable with visible focus", "Screen-reader compatible",
                            "Contrast and target sizes meet WCAG 2.2 AA"]))
    parts.append(h(2, "15. Performance Validation"))
    parts.append(checkboxes(["Performance budgets/SLOs met", "Tested under realistic load",
                            "No N+1 or unbounded queries"]))
    parts.append(h(2, "16. AI/LLM Validation"))
    parts.append(checkboxes(["Model outputs validated and guardrailed", "AI changes passed evaluation gate",
                            "No secrets/PII sent to models without controls"]))
    parts.append(h(2, "17. Documentation Validation"))
    parts.append(checkboxes(["Docs updated and accurate", "Examples provided where relevant",
                            "Cross-references valid"]))
    parts.append(h(2, "18. Compliance Validation"))
    parts.append(checkboxes(["Mapped to applicable controls", "Audit evidence captured",
                            "Findings tracked and within SLA"]))
    parts.append(h(2, "19. Deployment Readiness"))
    parts.append(checkboxes(["Release gates passed", "Monitoring/alerts in place", "On-call coverage confirmed"]))
    parts.append(h(2, "20. Rollback Readiness"))
    parts.append(checkboxes(["Rollback path defined and tested", "Data migration reversible or compensable",
                            "Rollback decision criteria documented"]))
    parts.append(h(2, "21. Common Failure Patterns"))
    parts.append(bullets(["Skipping items under deadline pressure.",
                          "Treating automated scans as full coverage.",
                          "Missing rollback or recovery validation."]))
    parts.append(h(2, "22. Escalation Process"))
    parts.append(f"Unresolved failures escalate to the {c['owner']}, then to engineering leadership. Security/Privacy/Compliance failures may block release outright.")
    parts.append(h(2, "23. Definition of Pass"))
    parts.append("Every applicable item is checked with evidence and no critical item is failing.")
    parts.append(h(2, "24. Definition of Fail"))
    parts.append("Any critical item fails, or evidence is missing for a required item.")
    parts.append(h(2, "25. Evidence Required"))
    parts.append(bullets(["Test/scan/eval reports", "Reviewer sign-offs", "Relevant dashboards or screenshots"]))
    parts.append(h(2, "26. Sign-off Matrix"))
    parts.append("\n".join(["| Role | Responsibility | Sign-off |", "| --- | --- | --- |",
                            f"| {c['owner']} | Owner | [ ] |",
                            "| Independent Reviewer | Verification | [ ] |",
                            "| Security (if applicable) | Security gate | [ ] |",
                            "| Release Manager | Gate decision | [ ] |"]))
    parts.append(h(2, "27. Metrics"))
    parts.append(bullets(["Pass rate", "Defect escape rate after gate", "Time to complete checklist"]))
    parts.append(h(2, "28. References"))
    parts.append(bullets([f"{x}" for x in stds] + ["Specification (../ASFE_SPECIFICATION.md)"]))
    parts.append(h(2, "29. Metadata"))
    parts.append("\n".join([f"- **Checklist ID:** {doc_id}", f"- **Owner:** {c['owner']}",
                            f"- **Category:** {c['category']}", f"- **Version:** {VERSION}",
                            "- **Status:** Active", "- **Review Frequency:** Quarterly",
                            f"- **Effective Date:** {TODAY}", f"- **Last Updated:** {TODAY}"]))
    return join_doc(parts)


# ---------------------------------------------------------------------------
# PLAYBOOKS
# ---------------------------------------------------------------------------
def gen_playbook(p: dict) -> str:
    title = humanize(p["name"])
    doc_id = slugify_id("PLAY", p["name"])
    parts = []
    parts.append(metadata_block(doc_id, p["owner"], p["category"], "High"))
    parts.append(h(1, f"PLAYBOOK — {title}"))
    parts.append(f"> Repeatable operational procedure owned by the {p['owner']}.")
    parts.append(h(2, "1. Purpose"))
    parts.append(f"Provide a consistent, tested procedure for **{title}**.")
    parts.append(h(2, "2. Objective"))
    parts.append(p["objective"])
    parts.append(h(2, "3. Trigger"))
    parts.append(p["trigger"])
    parts.append(h(2, "4. Roles"))
    parts.append(bullets(p["roles"]))
    parts.append(h(2, "5. Preconditions"))
    parts.append(bullets(["Required access, tooling, and runbooks are available.",
                          "Stakeholders and communication channels are known."]))
    parts.append(h(2, "6. Procedure"))
    parts.append(numbered(p["steps"]))
    parts.append(h(2, "7. Decision Points"))
    parts.append(bullets(["Escalate when impact or scope exceeds the responder's authority.",
                          "Choose mitigate-forward vs. roll back based on predefined criteria."]))
    parts.append(h(2, "8. Communication Plan"))
    parts.append(bullets(["Notify stakeholders at start, on status changes, and at resolution.",
                          "Use the designated incident/comms channel; keep a timeline."]))
    parts.append(h(2, "9. Rollback / Recovery"))
    parts.append(bullets(["Maintain a tested rollback or recovery path.",
                          "Verify recovery against SLIs and smoke tests."]))
    parts.append(h(2, "10. Post-Procedure Review"))
    parts.append(bullets(["Run a blameless review.", "Log owned, time-bound action items.",
                          "Update this playbook with lessons learned."]))
    parts.append(h(2, "11. Validation Checklist"))
    parts.append(checkboxes(["Trigger and roles are clear", "Each step is actionable and tested",
                            "Communication plan executed", "Rollback/recovery verified",
                            "Post-review completed with actions", "Metadata complete"]))
    parts.append(h(2, "12. Metrics"))
    parts.append(bullets(["Time to execute", "Success rate", "Recurrence rate", "Action-item closure"]))
    parts.append(h(2, "13. References"))
    parts.append(bullets(["Specification (../ASFE_SPECIFICATION.md)",
                          "Related checklists and runbooks in this repository."]))
    parts.append(h(2, "14. Metadata"))
    parts.append("\n".join([f"- **Playbook ID:** {doc_id}", f"- **Owner:** {p['owner']}",
                            f"- **Category:** {p['category']}", f"- **Version:** {VERSION}",
                            "- **Status:** Active", "- **Review Frequency:** Quarterly",
                            f"- **Created:** {TODAY}", f"- **Updated:** {TODAY}"]))
    return join_doc(parts)


# ---------------------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------------------
def gen_template(t: dict) -> str:
    title = humanize(t["name"])
    doc_id = slugify_id("TMPL", t["name"])
    parts = []
    parts.append(metadata_block(doc_id, "Technical Writer", "Documentation", "Medium"))
    parts.append(h(1, f"TEMPLATE — {title}"))
    parts.append(f"> {t['purpose']}")
    parts.append(h(2, "How to Use"))
    parts.append(bullets(["Copy this template into the appropriate folder.",
                          "Replace placeholder guidance in each section.",
                          "Complete the metadata front matter.",
                          "Validate against the framework specification before publishing."]))
    parts.append(h(2, "Front Matter"))
    parts.append("```yaml\n" + "\n".join([
        "---", "id: <DOC-ID>", "owner: <Owner>", "department: <Department>",
        f"version: {VERSION}", "status: Draft", "criticality: <Low|Medium|High|Critical>",
        "review_frequency: Quarterly", "classification: Internal",
        "created: <YYYY-MM-DD>", "updated: <YYYY-MM-DD>", "---",
    ]) + "\n```")
    parts.append(h(2, "Sections"))
    body = []
    for i, sec in enumerate(t["sections"], 1):
        body.append(f"### {i}. {sec}\n\n_Provide content for **{sec}** here._")
    parts.append("\n\n".join(body))
    parts.append(h(2, "Metadata"))
    parts.append("\n".join([f"- **Template ID:** {doc_id}", "- **Owner:** Technical Writer",
                            f"- **Version:** {VERSION}", "- **Status:** Active",
                            f"- **Created:** {TODAY}", f"- **Updated:** {TODAY}"]))
    return join_doc(parts)


# ---------------------------------------------------------------------------
# KNOWLEDGE
# ---------------------------------------------------------------------------
def gen_knowledge(k: dict) -> str:
    title = humanize(k["name"])
    doc_id = slugify_id("KB", k["name"])
    parts = []
    parts.append(metadata_block(doc_id, "Enterprise Architect", "Knowledge", "Medium", review="Annually"))
    parts.append(h(1, f"KNOWLEDGE — {title}"))
    parts.append(f"> {k['summary']}")
    parts.append(h(2, "1. Summary"))
    parts.append(k["summary"])
    parts.append(h(2, "2. Context"))
    parts.append("Curated reference knowledge for teams building SaaS products.")
    parts.append(h(2, "3. Key Concepts"))
    parts.append(bullets(k["concepts"]))
    parts.append(h(2, "4. Guidance"))
    parts.append(bullets(k["guidance"]))
    parts.append(h(2, "5. Pitfalls"))
    parts.append(bullets(k["pitfalls"]))
    parts.append(h(2, "6. Related Documents"))
    parts.append(bullets(["Specification (../ASFE_SPECIFICATION.md)",
                          "Relevant Rules, Skills, and Checklists in this repository."]))
    parts.append(h(2, "7. References"))
    parts.append(bullets(["Official standards and primary sources (see Standards Index)."]))
    parts.append(h(2, "8. Metadata"))
    parts.append("\n".join([f"- **Knowledge ID:** {doc_id}", "- **Owner:** Enterprise Architect",
                            f"- **Version:** {VERSION}", "- **Status:** Active",
                            "- **Review Frequency:** Annually",
                            f"- **Created:** {TODAY}", f"- **Updated:** {TODAY}"]))
    return join_doc(parts)


# ---------------------------------------------------------------------------
# DEPARTMENT INDEX + ROOT
# ---------------------------------------------------------------------------
def gen_department_index(code: str, title: str, desc: str) -> str:
    related_skills = [s for s in SKILLS if s["dept"] == code]
    parts = []
    parts.append(h(1, f"{code} — {title}"))
    parts.append(desc)
    parts.append(h(2, "Mandate"))
    parts.append(f"The {title} department upholds the framework specification and cross-cutting principles within its domain.")
    if related_skills:
        parts.append(h(2, "Specialists (Skills)"))
        parts.append(bullets([f"[{humanize(s['name'])}](../Skills/{s['name']}.md)" for s in related_skills]))
    parts.append(h(2, "Cross-cutting Principles"))
    parts.append(bullets(CROSS_CUTTING_PRINCIPLES))

    assets = assets_for_department(code)
    parts.append(h(2, "Related Assets"))
    parts.append(f"Documents directly relevant to the {title} department. "
                 "Browse the full libraries: "
                 "[Rules](../Rules/) · [Checklists](../Checklists/) · "
                 "[Playbooks](../Playbooks/) · [Templates](../Templates/) · "
                 "[Knowledge](../Knowledge/).")

    def link_list(items, folder):
        return bullets([f"[{humanize(i['name'])}](../{folder}/{i['name']}.md)" for i in items])

    if assets["rules"]:
        parts.append(h(3, "Rules"))
        parts.append(link_list(assets["rules"], "Rules"))
    if assets["checklists"]:
        parts.append(h(3, "Checklists"))
        parts.append(link_list(assets["checklists"], "Checklists"))
    if assets["playbooks"]:
        parts.append(h(3, "Playbooks"))
        parts.append(link_list(assets["playbooks"], "Playbooks"))
    if assets["templates"]:
        parts.append(h(3, "Templates"))
        parts.append(link_list(assets["templates"], "Templates"))
    if assets["knowledge"]:
        parts.append(h(3, "Knowledge"))
        parts.append(link_list(assets["knowledge"], "Knowledge"))
    return join_doc(parts)


def gen_root_readme(counts: dict) -> str:
    dept_rows = "\n".join([f"| `{code}` | {DEPT_BY_CODE[code][0]} | {DEPT_BY_CODE[code][1]} |"
                           for code, _, _ in DEPARTMENTS])
    skills_list = "\n".join([f"- [{humanize(s['name'])}](Skills/{s['name']}.md) — {DEPT_BY_CODE[s['dept']][0]}"
                             for s in SKILLS])
    rules_list = "\n".join([f"- [{humanize(r['name'])}](Rules/{r['name']}.md)" for r in RULES])
    chk_list = "\n".join([f"- [{humanize(c['name'])}](Checklists/{c['name']}.md)" for c in CHECKLISTS])
    play_list = "\n".join([f"- [{humanize(p['name'])}](Playbooks/{p['name']}.md)" for p in PLAYBOOKS])
    tmpl_list = "\n".join([f"- [{humanize(t['name'])}](Templates/{t['name']}.md)" for t in TEMPLATES])
    kb_list = "\n".join([f"- [{humanize(k['name'])}](Knowledge/{k['name']}.md)" for k in KNOWLEDGE])
    return f"""# {FRAMEWORK_NAME} ({FRAMEWORK_ABBR})

**A reusable AI engineering operating system for building production-grade SaaS products with AI assistants and human engineers.**

Version: {VERSION} · Generated: {TODAY}

{FRAMEWORK_ABBR} is the single source of truth governing product engineering, AI engineering,
architecture, security, DevSecOps, quality, cloud, operations, growth, and governance.
Every document is **Documentation-as-Code**: generated from versioned data tables and
the master prompts in [`_generators/`](_generators/), regenerable via
[`_build/generate_asfe.py`](_build/generate_asfe.py).

> **Reusing a single file?** Individual Skills, Rules, Checklists, Playbooks, Templates,
> and Knowledge articles are written to be framework-neutral, so you can lift any one of
> them into your own project. The {FRAMEWORK_ABBR} brand lives only here, in the
> specification, and in each document's front-matter `framework` field.

---

## Contents

| Type | Count |
| --- | --- |
| Specialist Skills | {counts['skills']} |
| Engineering Rules | {counts['rules']} |
| Quality Checklists | {counts['checklists']} |
| Operational Playbooks | {counts['playbooks']} |
| Document Templates | {counts['templates']} |
| Knowledge Articles | {counts['knowledge']} |
| Department Indexes | {counts['departments']} |
| **Total Markdown documents** | **{counts['total']}** |

---

## Repository Structure

| Folder | Department | Focus |
| --- | --- | --- |
{dept_rows}

Cross-cutting asset folders: `Skills/`, `Rules/`, `Checklists/`, `Playbooks/`, `Templates/`, `Knowledge/`.

---

## Guiding Principles

{bullets(CROSS_CUTTING_PRINCIPLES)}

---

## Document Types

1. **SKILLS.md** — specialist responsibilities, authority, and standards.
2. **RULES.md** — mandatory, enforceable engineering standards.
3. **CHECKLIST.md** — auditable quality gates.
4. **PLAYBOOK.md** — repeatable operational procedures.
5. **TEMPLATE.md** — reusable document scaffolds.
6. **KNOWLEDGE.md** — curated technical reference.

---

## Quality Gates

Every feature flows through:
Idea → Product → Architecture → Security → AI → Backend → Frontend → QA → Performance → Accessibility → SEO/AEO/GEO → Release → Production.

---

## Skills

{skills_list}

## Rules

{rules_list}

## Checklists

{chk_list}

## Playbooks

{play_list}

## Templates

{tmpl_list}

## Knowledge

{kb_list}

---

## Regenerating

```bash
python3 _build/generate_asfe.py
```

All content is deterministic and reproducible from `_build/` data tables.

---

## License & Status

Internal engineering operating system. See [`ASFE_SPECIFICATION.md`](ASFE_SPECIFICATION.md) for governance.
"""


def main():
    counts = {}
    for s in SKILLS:
        write(f"Skills/{s['name']}.md", gen_skill(s))
    counts["skills"] = len(SKILLS)

    for r in RULES:
        write(f"Rules/{r['name']}.md", gen_rule(r))
    counts["rules"] = len(RULES)

    for c in CHECKLISTS:
        write(f"Checklists/{c['name']}.md", gen_checklist(c))
    counts["checklists"] = len(CHECKLISTS)

    for p in PLAYBOOKS:
        write(f"Playbooks/{p['name']}.md", gen_playbook(p))
    counts["playbooks"] = len(PLAYBOOKS)

    for t in TEMPLATES:
        write(f"Templates/{t['name']}.md", gen_template(t))
    counts["templates"] = len(TEMPLATES)

    for k in KNOWLEDGE:
        write(f"Knowledge/{k['name']}.md", gen_knowledge(k))
    counts["knowledge"] = len(KNOWLEDGE)

    for code, title, desc in DEPARTMENTS:
        write(f"{code}/README.md", gen_department_index(code, title, desc))
    counts["departments"] = len(DEPARTMENTS)

    counts["total"] = (counts["skills"] + counts["rules"] + counts["checklists"] +
                       counts["playbooks"] + counts["templates"] + counts["knowledge"] +
                       counts["departments"] + 2)  # +root README +spec

    write("README.md", gen_root_readme(counts))

    print(f"Generated {len(WRITTEN)} files (excluding spec, written separately).")
    for k, v in counts.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
