"""ASFE Documentation-as-Code: shared helpers, metadata, and reference data.

This module is imported by the document generators. It centralises the
cross-cutting principles, standards mappings, universal metadata, and the
authoritative lists of departments and document types so every generated
Markdown file is structurally consistent with the ASFE master prompts.
"""

from __future__ import annotations

import datetime as _dt

VERSION = "1.0.0"
TODAY = _dt.date.today().isoformat()

# ---------------------------------------------------------------------------
# Cross-cutting principles enforced by every document (from the master prompts)
# ---------------------------------------------------------------------------
CROSS_CUTTING_PRINCIPLES = [
    "Security by Design",
    "Privacy by Design",
    "Accessibility by Default",
    "Performance First",
    "Observability First",
    "API First",
    "Cloud Native",
    "Zero Trust",
    "Principle of Least Privilege",
    "Secure Defaults",
    "Testability",
    "Documentation as Code",
    "Automation First",
    "Backward Compatibility",
]

# Standards catalogue keyed by domain tag, used to assemble per-document mappings.
STANDARDS = {
    "security": [
        "OWASP ASVS", "OWASP Top 10", "OWASP API Security Top 10", "NIST CSF",
        "NIST SP 800-53", "CIS Controls", "ISO/IEC 27001", "SOC 2 Type II",
    ],
    "privacy": ["GDPR", "CCPA/CPRA", "ISO/IEC 27701", "NIST Privacy Framework"],
    "frontend": ["WCAG 2.2 AA", "Core Web Vitals", "HTML Living Standard", "ECMAScript", "React"],
    "backend": ["REST", "OpenAPI 3.1", "RFC 9110 (HTTP)", "Twelve-Factor App", "OAuth 2.1", "OIDC"],
    "api": ["OpenAPI 3.1", "JSON:API", "RFC 9457 (Problem Details)", "OAuth 2.1", "AsyncAPI"],
    "ai": ["NIST AI RMF", "ISO/IEC 42001", "OWASP LLM Top 10", "Model Context Protocol (MCP)"],
    "eval": ["RAGAS", "DeepEval", "OWASP LLM Top 10", "NIST AI RMF"],
    "data": ["ISO/IEC 11179", "DCAM", "GDPR", "Data Mesh principles"],
    "cloud": ["Twelve-Factor App", "CIS Benchmarks", "AWS/Azure/GCP Well-Architected", "OpenTelemetry"],
    "observability": ["OpenTelemetry", "Google SRE (SLO/SLI)", "RED/USE methods"],
    "quality": ["ISTQB", "IEEE 829", "Test Pyramid", "Twelve-Factor App"],
    "performance": ["Core Web Vitals", "RAIL model", "Web Vitals", "OpenTelemetry"],
    "accessibility": ["WCAG 2.2 AA", "WAI-ARIA 1.2", "EN 301 549", "Section 508"],
    "compliance": ["SOC 2 Type II", "ISO/IEC 27001", "GDPR", "PCI DSS 4.0"],
    "finance": ["ASC 606 / IFRS 15", "SaaS metrics (ARR, NRR, CAC, LTV)", "PCI DSS 4.0"],
    "growth": ["Schema.org", "Core Web Vitals", "Google Search Essentials", "GA4"],
    "release": ["SemVer 2.0.0", "Conventional Commits", "DORA metrics", "Twelve-Factor App"],
    "general": ["Twelve-Factor App", "SemVer 2.0.0", "Conventional Commits"],
}

# v2 numbered department structure (BUILD_ASFE_V2_MASTER_PROMPT).
DEPARTMENTS = [
    ("00_Governance", "Governance", "Enterprise governance, document lifecycle, RACI, and quality-gate ownership."),
    ("01_Executive", "Executive", "Strategy, vision, OKRs, and cross-department alignment."),
    ("02_Product", "Product", "Product strategy, requirements, roadmap, and documentation."),
    ("03_UX", "UX", "User research, interaction design, and usability."),
    ("04_Frontend", "Frontend", "Client applications, design system, and accessibility delivery."),
    ("05_Backend", "Backend", "Services, business logic, and server-side reliability."),
    ("06_AI", "AI", "AI/LLM engineering, prompting, safety, and evaluation."),
    ("07_RAG", "RAG", "Retrieval-augmented generation pipelines and knowledge grounding."),
    ("08_Data", "Data", "Data modelling, pipelines, governance, and analytics."),
    ("09_Database", "Database", "Database architecture, schema design, and migrations."),
    ("10_API", "API", "API design, contracts, versioning, and governance."),
    ("11_Cloud", "Cloud", "Cloud architecture, networking, and well-architected design."),
    ("12_DevOps", "DevOps", "CI/CD, infrastructure as code, and automation."),
    ("13_DevSecOps", "DevSecOps", "Security automation across the delivery pipeline."),
    ("14_Security", "Security", "Application and platform security engineering."),
    ("15_Privacy", "Privacy", "Data protection, privacy engineering, and DPIAs."),
    ("16_Compliance", "Compliance", "Audit readiness, controls, and certifications."),
    ("17_QA", "QA", "Quality engineering, test strategy, and accessibility QA."),
    ("18_Performance", "Performance", "Performance engineering and capacity planning."),
    ("19_Observability", "Observability", "Telemetry, monitoring, SLOs, and alerting."),
    ("20_SEO", "SEO", "SEO, AEO, and GEO discoverability engineering."),
    ("21_Marketing", "Marketing", "Product and growth marketing."),
    ("22_Sales", "Sales", "Sales enablement and revenue operations."),
    ("23_CustomerSuccess", "Customer Success", "Onboarding, retention, and customer health."),
    ("24_Finance", "Finance", "SaaS finance, billing, and payments."),
    ("25_Legal", "Legal", "Contracts, licensing, and regulatory counsel."),
    ("26_Release", "Release", "Release management and change control."),
    ("27_Operations", "Operations", "Site reliability and production operations."),
]


def front_matter(meta: dict) -> str:
    """Render an ordered YAML front-matter block."""
    lines = ["---"]
    for key, value in meta.items():
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                rendered = ", ".join(str(v) for v in value)
                lines.append(f"{key}: [{rendered}]")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def h(level: int, text: str) -> str:
    return f"{'#' * level} {text}"


def bullets(items) -> str:
    return "\n".join(f"- {i}" for i in items)


def numbered(items) -> str:
    return "\n".join(f"{n}. {item}" for n, item in enumerate(items, 1))


def checkboxes(items) -> str:
    return "\n".join(f"- [ ] {i}" for i in items)


def hr() -> str:
    return "\n---\n"


def standards_for(*tags) -> list:
    """Merge standards lists for the given domain tags, de-duplicated, order-stable."""
    seen, out = set(), []
    for tag in tags:
        for s in STANDARDS.get(tag, []):
            if s not in seen:
                seen.add(s)
                out.append(s)
    return out


def slugify_id(prefix: str, name: str) -> str:
    base = "".join(c for c in name if c.isalnum() or c in "_ ").strip().replace(" ", "_")
    return f"{prefix}-{base.upper()}"
