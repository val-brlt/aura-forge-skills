# Functional documents independent of release planning

Use with [versioning.md](versioning.md). French for user-facing content; preserve English metadata, stable IDs, filenames and original-language approved summaries.

## Paths and compatibility adapter

Discover DOCS_ROOT; reuse it. Maintain `PROJECT.md`, `MVP.md`, `FUTURE-FEATURES.md`, `modules/<module>/MODULE.md` and one canonical feature card per FEAT. A new global MVP does not need `versions/` or a target software version. Keep its approved `SCOPING-SUMMARY.md` at the existing scope location, or DOCS_ROOT for a new project. Use `.scratch/project-scoping/<project>/<scope-id>/` without allocating a version.

`structure-project` remains useful for catalogue methodology and **legacy read-only audits**, but its current `target_version`, `release_kind=mvp`, MVP-pointer and V1/V2 templates are legacy-only. For this workflow, this reference and `versioning.md` govern its preview/apply/audit procedures: supply `scope_id`, `scope_kind`, approved summary path and DOCS_ROOT; `target_version` is optional and only records an already-approved release assignment. Never use the legacy apply templates or their validator to force MVP features into `versions/v1/`, manufacture a version or reduce `MVP.md` to a pointer. Execute the following adapted procedures directly; no separate skill invocation tool is required. Updating `structure-project` as an independent entry point is a separate compatibility task, not an implicit migration here.

## Preview → apply → audit (preserve every approval gate)

1. **Preview (read-only):** read approved summary, project/MVP/backlog, relevant cards and legacy scopes. Reuse IDs and module slugs. Show module, FEAT, French name, new/evolution, functional scope, independent progress fields, provenance, acceptance criteria, dependencies, unresolved/rejected proposals, exact manifest and diffs to existing approved prose. Keep proposals outside the approved MVP. Wait for explicit catalogue approval.
2. **Apply:** preserve the approved summary verbatim; update the same canonical cards/modules, living project/MVP/backlog and source links. Create only approved functional content, with documentation `status: draft` until final review. Amend ordinary sections, not appendix-style change paragraphs. Preserve earlier delivered requirements in attributable baseline sections. For an undelivered approved scope, require a visible, explicit correction approval before changing its approved requirements. Never manufacture acceptance criteria or reclassify backlog items as approved.
3. **Audit (read-only):** run `python .agents/skills/project-scoping/scripts/validate_scope.py <DOCS_ROOT> --scope MVP.md` (or the actual functional source). It checks unique FEAT IDs, canonical cards, module/PROJECT/MVP/backlog links, source paths, scope approval metadata and acceptance criteria without requiring release folders. For new cards use a `## Critères d'acceptation validés` section. For unchanged legacy trees retain the legacy structural audit rather than forcing new headings. Manually verify French prose, approval authority, progress/evidence, partial slices and preservation of delivered criteria. Cross-check functional/UX/technical dependencies without assigning releases; compare diff with approved preview. Run UX/architecture validators plus `python .agents/skills/project-scoping/scripts/validate_delivery.py <contract.json>` for delivery metadata. Record automated versus semantic/manual checks. The legacy structure validator does not certify the new global MVP format.
4. **Final documentation review:** present changed files, exact FEAT set, coverage, unresolved questions, warnings and scoped diff. Obtain explicit document approval; update only document approval metadata, never delivery. Return to the scoping orchestrator for separate commit and push gates.

## Canonical content

`PROJECT.md`: purpose/users, outcomes, product scope, module index, link to global MVP and future features; separate index of existing legacy scopes, approved release plans and actual release evidence. Link only existing files; no empty future-version folders.

`MVP.md` example (illustrative IDs only):

```markdown
---
scope_id: mvp
scope_kind: mvp
status: draft
source: SCOPING-SUMMARY.md
---
# Objectif MVP
## Objectifs et critères de réussite
<Critères fonctionnels explicitement approuvés>
## Fonctionnalités incluses
- [FEAT-001 — Créer un projet](modules/project-management/create-project.md)
## Dépendances et décisions ouvertes
<Dépendances FEAT et questions non résolues>
## Limites et exclusions
<Fonctionnalités futures dans FUTURE-FEATURES.md>
## Avancement de l'objectif MVP
<Jalon ouvert ; preuves requises pour chaque critère ; aucune version imposée>
## Source de cadrage
[Synthèse validée](SCOPING-SUMMARY.md)
```

Canonical feature metadata retains `id`, `module`, `decision_status`, `source`. Add `scope: mvp` or `future` where approved; do not infer it from `release_bucket`. In prose keep `Objectif utilisateur`, `Comportement attendu`, approved acceptance criteria, `Dépendances fonctionnelles`, `Questions ouvertes`, source traceability and attributable delivered baseline sections. Record planning, development and delivery separately, explicitly unknown when unverified. Describe incomplete slices and remaining criteria without renaming the feature. Existing historical version headings remain intact; new requirements need no artificial version heading.

`MODULE.md`: purpose, functional responsibilities, links to canonical features and dependencies. `FUTURE-FEATURES.md`: deferred enhancements, approved future concepts with no schedule, proposals/unresolved decisions and rejected items separately. A pending enhancement may reuse an existing FEAT; name the pending change rather than relabeling the entire shipped feature.

Existing `versions/<legacy-id>/VERSION.md` and summaries remain approved scope baselines at their current paths, not inferred releases. After actual planning approval, a new `versions/<X.Y.Z>/VERSION.md` may index release changes/slices, acceptance and dependencies, baseline, compatibility and evidence; keep `status` for document approval and record actual delivery separately. `release_kind` on old documents remains historical; do not generate `release_kind: mvp` for new releases.
