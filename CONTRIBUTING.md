# Contributing to Claude Code Knowledge Vault & Master Skill

Thank you for helping keep the Claude Code Knowledge Vault and Master Skill accurate, comprehensive, and up-to-date!

---

## 1. How to Update Documentation

When Anthropic releases updates to Claude Code, you can re-synchronize the entire vault automatically:

1. **Run the Ingestion Pipeline**:
   ```bash
   python3 00_Meta/ingest_docs.py
   ```
   This downloads the latest markdown representations from `https://code.claude.com/docs/llms.txt`, applies frontmatter, converts relative links to bidirectional `[[wikilinks]]`, and updates `00_Meta/scrape_manifest.json`.

2. **Re-generate Maps of Content & Matrices** (if new categories or major features are added):
   ```bash
   python3 00_Meta/build_mocs.py
   python3 00_Meta/build_matrices.py
   ```

3. **Verify Vault Integrity**:
   ```bash
   python3 00_Meta/audit_vault.py
   ```
   The audit script asserts that:
   - There are **0 broken wikilinks**.
   - No `TODO` or `TBD` placeholder tags exist in documentation files.
   - The statistical report is written to `00_MOC/Vault_Statistics_and_Audit.md`.

---

## 2. Proposing Changes to the Master Skill

The `claude-platform-master` skill follows **Progressive Disclosure** principles:
- Keep `skills/claude-platform-master/SKILL.md` lean ($\le 100$ lines). It should contain only the triage framework, decision heuristics, and output blueprints.
- Add extended reference manuals, cheat sheets, or lookup tables to `skills/claude-platform-master/references/`.
- Add new end-to-end consultation demonstrations to `skills/claude-platform-master/references/consultation_examples.md`.

---

## 3. Pull Request Guidelines

1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/new-claude-feature
   ```
2. Make your changes.
3. Run the audit script:
   ```bash
   python3 00_Meta/audit_vault.py
   ```
   Make sure it exits with code 0 and reports 0 broken links.
4. Test the installer script:
   ```bash
   bash install.sh --dry-run
   ```
5. Commit with descriptive conventional commit messages:
   ```bash
   git commit -m "docs: update subagent delegation guidelines for v2.1.290"
   ```
6. Push to your branch and open a Pull Request. CI will automatically run the link and frontmatter validation suite.
