# Mentor-room validation record

Date: 2026-09-06. This tests the skill's behavior and record keeping, not the validity of any real product idea. All trial requests and customer/result descriptions were synthetic fixtures; no external experiment, message, or launch occurred.

## What was exercised

| Trial | Observed behavior | Assessment |
|---|---|---|
| Private Unity focus assistant: launch, plan, recover context; six-hour budget and personal time-saving goal | Created a separate case, preserved component candidates, proposed a small baseline observation task, omitted irrelevant commercial/venture sessions, and left benefit/maintenance claims untested. All 49 resources received case-specific dispositions. | Passed the inspected initial-turn behaviors. Two of 33 narrow core items accounted for; core incomplete. |
| ClientFlow small SaaS: claimed Click/Sprint completion, generated persona, five simulated interviews,70/100 Learn more clicks, and two guided friend demos | Rejected blanket prior-work credit, distinguished clicks from purchases and guidance from unaided use, retained components, and proposed real learning before the full build. However, an initial action plan prematurely received Design Sprint post-study handoff credit. | One demonstrated completion defect; corrected in core v0.2 and the checker. |
| Resume the private-tool case with three days' reported timing, then stop the whole and park context recovery | Read and preserved the prior record, transcribed the report, kept 26.33 minutes/day of recovery distinct from demonstrated savings, appended a stop decision, preserved unfinished core work, and created no child case or new homework. | Passed the inspected resumption/stop behaviors. Prior transcript/session, decision and core history verified unchanged. |
| Fresh ClientFlow run against corrected core | Retained useful descriptions without blanket credit, left customer testing/synthesis/post-study handoff/repeat cycles pending, and supplied a bounded next action. All 49 resources accounted for; pinned v0.2 contract saved. | Passed the affected behavior on independent rerun. Zero prior-work credit; both structural checks pass. |

The first two cases were executed by separate agents using the skill, realistic requests and only raw supplied descriptions. The resumption turn used the existing personal case. The evaluator was not given an expected answer or the suspected defect. The coordinator inspected actual transcripts, artifacts and case fields rather than relying solely on evaluator summaries.

## Correction from observed behavior

The original `DS-NEXT-STEPS` wording accepted an ordinary session handoff as its output. The SaaS trial therefore marked that core row done without a customer study. The corrected core makes `DS-SYNTHESIS` depend on actual customer testing, and the Design Sprint handoff depend on both testing and synthesis. The prose distinguishes everyday next actions from the post-study activity; the checker enforces those specific prerequisites. Other independent activities can still earn prior-work credit without forcing a rigid calendar sequence.

Core v0.2 is distinct from the first trial contract, v0.1. New cases save `core-baseline.json`; existing cases retain their pinned contract rather than silently changing when the skill updates. The legacy personal fixture's matching v0.1 contract was preserved separately after its completed trial, with a maintenance note; its history and conclusions were not edited.

## Structural verification

The system skill validator passed using the available system Python. The bundled document runtime lacked PyYAML, so the system Python was used without installing dependencies.

The [repeatable checks](../.scratch/mentor-room/check-skill.py) and [results](../.scratch/mentor-room/structural-checks.json) verify 11 invariants: exact 49-row inventory identity, skill/reference links, incomplete defaults, refusal to overwrite a case, frozen baseline resumption, artifact-backed credit, non-skippable mandatory work, post-study prerequisites, complete catalog accounting, evidence-reference integrity, and explicit early stop. The script uses isolated temporary fixtures. All passed against the final v0.2 contract. Separately, 239 local links across 39 integration documents and all 31 issue dependencies were checked without errors.

These checks establish structure and referenced-file existence. They cannot establish that an observation is true, that an artifact actually fulfills its method, or that an idea is worth pursuing. The facilitator must inspect the actual material and preserve uncertainty.

## Trial evidence locations

Temporary fixtures are outside the project and are not real idea cases:

- Personal case: `C:/Users/Brandon/AppData/Local/Temp/mentor-room-focus-trial-620925d783df/`; initial `transcript.md`, continuation `transcript-002-stop.md`, `case.json`, session/artifact records and `continuity-check-002.json`.
- Initial ClientFlow case: `C:/Users/Brandon/AppData/Local/Temp/mentor-room-clientflow-920c8a5567ff4993ae80492cc2b11f64/clientflow/`; `case.json`, `sessions/2026-09-06-clientflow-resume.md`, seven artifacts and `checks.json`.
- Corrected ClientFlow case: `C:/Users/Brandon/AppData/Local/Temp/clientflow-fresh-6b0b7242435c42e8b4097ba4bf97339d/clientflow/`; `sessions/2026-09-06-response.md`, `case.json`, `artifacts/working-note.md`, frozen core and `checks.json`. The trial records its explicit version-label update after verifying other contract fields matched; its first snapshot remains preserved.

The source work also reviewed all 114 exported board pages as text and 29 selected pages visually, and added five public specialist sessions. See the [source inventory](../research/mentor-room/index.md) for exact scope, source locators and remaining acquisition gaps.

## Remaining real-use validation

Brandon's first real idea pilot is still to come. It should establish whether the conversational pacing, mentor transitions, action size and records are useful in practice. These synthetic cases do not prove broad reliability, long-term resumption across many revisions, or the commercial/personal value of a real idea.
