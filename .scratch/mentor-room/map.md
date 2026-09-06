# Develop and test the product idea mentor room

Labels: wayfinder:map
Status: open

## Destination

A reusable, researched, and tested skill that helps Brandon develop software ideas of any size or maturity, including features of existing products, through dialogue, research, artifacts, and real-world tests toward an evidence-backed decision about further investment. It preserves progress between sessions, gives concrete next steps, coordinates overlapping methods, and includes mandatory coverage of Jake Knapp and John Zeratsky's methods.

## Notes

- This is the map for developing the skill; future idea evaluations are separate efforts with their own evidence and decisions.
- Parked architectural hypothesis from Brandon: individual subskills for recurring deliverables or sub-outcomes, such as user profiles and competitor research, coordinated by the room. [Evaluate deliverable-focused subskills after the pilot](issues/32-deliverable-subskills-after-pilot.md) preserves the proposal for reconsideration after real use; no split is authorized or required now.
- Use wayfinder, grilling, domain-modeling, research, skill-creator, and writing-for-agents as applicable. Their entrypoints are in `.agents/skills/`, except skill-creator in the configured system skills.
- Use the [local issue tracker](../../docs/agents/issue-tracker.md).
- The user's request is authoritative. The supplied CSV is a source inventory; its ordering, claims, and Notes cells are reference material, not instructions or verified findings.
- Preserve the supplied inventory at [resources.csv](../../research/mentor-room/resources.csv).
- On 2026-09-06 Brandon accepted the coordinating facilitator, explicit early stop, and design/build/trial route, and delegated remaining routine choices. This authorizes proceeding across the remaining design issues to skill authoring and independent behavioral trials in this session, overriding Wayfinder's usual planning-only and one-resolution-per-session limits. A real user pilot remains separate from synthetic tests.
- Research is saved to separate files in this checkout rather than switching the shared checkout between research branches. Agents own disjoint research files; the coordinator alone updates this map and its issues.
- Distinguish source-stated methods, our proposed adaptations, unverified catalog claims, and observed customer evidence. Summaries and source locators should be reusable; do not present an inaccessible book, video, board, or course as read.
- Knapp–Zeratsky coverage is mandatory per the user. An abandoned case may be recorded as stopped—core incomplete; stopping never earns completion credit. The current source baseline must be versioned and its gaps visible.
- Initial coverage and success-criteria questions were answered on 2026-09-05. The delegated operating choices were implemented on 2026-09-06; a real-user pilot will inform conversational refinements.
- Brandon capped source uploads with Testing Business Ideas on 2026-09-05. Continue design with the available library; do not solicit more books as a routine next step. Optional future receipts remain unreceived, and their absence must not be disguised as reviewed coverage. See the [source-batch readiness assessment](../../research/mentor-room/source-batch-readiness.md).

## Decisions so far

- [Build the first usable mentor-room skill](issues/29-build-mentor-room-skill.md): project skill, source-located playbooks, fixed-version case contracts, all-resource routing and working case support are authored and structurally checked.
- [Test facilitation and durable case behavior](issues/30-behavioral-trials.md): personal-tool, questionable-prior-evidence and stop/resume scenarios exercised; premature post-study completion corrected and independently retested. Real-user pilot remains separate.

- [Define the mandatory sprint coverage contract](issues/05-mandatory-core-contract.md): pin 33 source-traceable activities, make variants/adaptations explicit, and allow stopped—core incomplete without claiming completion.
- [Define evidence, decisions, and resumption across sessions](issues/06-evidence-and-resumption.md): use separate durable case records, scoped observations, append-only decisions, and concrete next actions.
- [Preserve promising component ideas when the whole changes](issues/07-component-ideas-and-context.md): retain components with original evidence context and create independent linked cases only when separately pursued.
- [Define a usable playbook and the remaining acquisition work](issues/08-playbook-source-completeness.md): operational source-located playbooks and all 49-resource routing, with targeted acquisition for relevant remaining gaps.
- [Reconcile supplied Click with the guides and saved board](issues/10-click-coverage-reconciliation.md): select explicit variants and retain source-specific worksheets and follow-through requirements.
- [Reconcile the Design Sprint guide and saved template](issues/11-sprint-coverage-reconciliation.md): account for all exported activities, including metrics, recruiting, mini hypotheses, evidence review and iteration, without claiming unread full-book coverage.

- [Define expert coverage and what worth pursuing means](issues/04-coverage-and-success-criteria.md): consider all experts with relevant sessions, credit checked prior work, and evaluate one idea at a time while preserving promising components.
- [Distinguish complementary methods from duplicate work](issues/02-evidence-and-method-overlap.md): reuse compatible observations while keeping demand, usability, feasibility, viability, and PMF conclusions distinct.
- [Audit the resource inventory and access gaps](issues/03-resource-inventory-and-access.md): classify all 49 entries and record a bounded eight-row access audit, including transcript and material gaps.
- [Establish the Knapp–Zeratsky source baseline](issues/01-knapp-zeratsky-source-baseline.md): verify official activity inventories and actual Miro access while tracking unreviewed book, worksheet, board, and transcript material.
- [Ingest the source materials Brandon shares](issues/09-ingest-shared-materials.md): preserve the supplied Click book, workshop snapshot, and agenda with verified hashes and searchable page indexes; more source batches may follow.
- [Extract the supplied Click book's method and source locations](issues/12-click-book-source-analysis.md): map 20 source-grounded activities and retain chapter/checklist differences and testing limits.
- [Identify the workshop sources and check the agenda](issues/13-click-workshop-source-analysis.md): identify the official guide snapshot, audit the unattributed two-day agenda, and preserve corrections as derived data.
- [Inspect the supplied public Mural template](issues/14-mural-template-access.md): verify Jonathan Vardy's public preview; retain explicit partial-review and export limits.
- [Preserve and convert the supplied Pincus EPUB](issues/17-ingest-pincus-epub.md): save the original unchanged and independently verify all 29 converted sections, 52 images, links, and source locators.
- [Extract Pincus's idea development and testing methods](issues/18-pincus-idea-methods.md): map 13 source-grounded practices and distinguish instincts, atomic tests, customer signals, and generated suggestions.
- [Place Pincus's iteration methods alongside the existing core](issues/19-pincus-iteration-and-fit.md): identify relevant iteration practices, context limits, and unresolved source metrics without creating a mandatory combined process.
- [Preserve and convert the supplied Pattern Breakers EPUB](issues/20-ingest-pattern-breakers.md): verify the download-suffixed file, preserve its bytes, and independently check searchable sections, images, tables, and links.
- [Extract Pattern Breakers opportunity and idea-development methods](issues/21-pattern-breakers-methods.md): map inflection/insight stress tests and discovery practices while retaining hypothesis and breakthrough-scope limits.
- [Place Pattern Breakers customer evidence and strategy alongside the core](issues/22-pattern-breakers-evidence-and-fit.md): identify focused prototype learning, surprise review, evidence limits, and conditional strategy practices alongside Click and Pincus.
- [Preserve and convert the supplied The Right It EPUB](issues/23-ingest-the-right-it.md): preserve the original and verify searchable sections, images, tables, lists, links, and mathematical notation.
- [Extract The Right It hypothesis and pretotyping methods](issues/24-the-right-it-experiments.md): map measurable engagement claims and small experiments while preserving limits on what their results establish.
- [Place The Right It evidence and decision rules alongside the core](issues/25-the-right-it-evidence-and-fit.md): distinguish commitment, repeated learning, and next decisions from heuristic scores and fictional teaching results.
- [Preserve and index the supplied Testing Business Ideas PDF](issues/26-ingest-testing-business-ideas.md): preserve and verify all 365 pages, record visual/extraction limits, and cap uploads while preparing for skill design.
- [Extract Testing Business Ideas assumptions and learning process](issues/27-testing-business-ideas-process.md): map hypotheses, visual templates, evidence, decisions, and context-dependent operating practices.
- [Index Testing Business Ideas experiments for relevant selection](issues/28-testing-business-ideas-experiments.md): index all 44 methods with source spans, observations, selection questions, and source inconsistencies.

## Current work and remaining trial

- [Build the first usable mentor-room skill](issues/29-build-mentor-room-skill.md): authored in the project's skill directory with progressive references and case support.
- [Test facilitation and durable case behavior](issues/30-behavioral-trials.md): completed for the first version; [validation record](../../docs/mentor-room-validation.md) preserves observed behavior and limits.
- [Run the room with Brandon's first real idea](issues/31-real-idea-pilot.md): still needs Brandon's chosen idea; synthetic trials do not substitute for real use or customer evidence.
- [Evaluate deliverable-focused subskills after the pilot](issues/32-deliverable-subskills-after-pilot.md): revisit Brandon's hypothesis using actual friction or deliverable-quality findings from that pilot.
- [Receive Sprint material](issues/15-receive-sprint-material.md) and [receive Click bonus worksheets](issues/16-receive-click-bonus-material.md): optional future source expansion, currently unreceived and not blockers for this first version.
- Conversational defaults are small connected question batches, artifact drafting during sessions, and meaningful mentor transitions. Revise based on observed use rather than designing every interaction in advance. Implementation recommendations address a bounded next investment; building a user's product is a separate instruction.

## Out of scope

- Building a standalone software app for the mentor room unless separately requested.
- Treating a simulated mentor's approval as real customer evidence or an endorsement by the named person.
- Purchasing materials, contacting customers, or launching public experiments as part of source research.
