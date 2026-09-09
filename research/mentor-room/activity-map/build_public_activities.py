"""Compact source summaries plus explicitly proposed activity/skill designs.

This file is editorial data, not a scraper or an attempt to reconstruct unavailable books.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources, activities, coverage = [], [], []

def source(id, title, url, scope, limitation='Public text only; linked books, videos, courses and templates are separate sources.'):
    sources.append(dict(id=id, title=title, kind='public_primary', path=url, coverage=scope, limitations=[limitation]))

def activity(id, title, src, category, purpose, steps, output, *, inputs=None, execution='dialogue', order='No required global order.', dependencies=None, independent='Can enter directly when the listed input exists; equivalent prior work can supply it.', idea=None, cautions=None, scope=None):
    # The workflow/AI fields below are our proposed design, not attributed author instructions.
    roles = {
        'dialogue': ('Ask focused questions, organize answers and flag unsupported claims.', 'Supply context, correct assumptions and choose the result.'),
        'ai_draft': ('Draft and compare an artifact from supplied evidence; retain provenance and missing fields.', 'Review factual accuracy and make consequential choices.'),
        'hybrid': ('Prepare the material and analyze supplied results; keep a checkpoint before field execution.', 'Arrange and conduct real interactions, supply observations and decide next actions.'),
        'human_fieldwork': ('Prepare a protocol and organize the results afterward.', 'Perform the real-world work and record what happened.'),
        'team_workshop': ('Facilitate prompts and synthesize separately captured contributions.', 'Participate independently and resolve the final team decision.'),
    }
    ai, human = roles[execution]
    activities.append(dict(
        id=id, title=title, source_id=src,
        source_ref=next(s['path'] for s in sources if s['id']==src)+' — '+(scope or title),
        category=category, kind='process' if len(steps)>6 else 'exercise', purpose=purpose,
        inputs=inputs or ['A relevant idea, product or decision context'], steps=steps,
        outputs=[{'artifact':output[0], 'fields':output[1:]}], source_order=order,
        prerequisites=dependencies or [], independence=independent, execution=execution,
        ai_role=ai, human_role=human,
        skill_idea=idea or 'Proposed: inspect existing work, ask only for missing context, draft this output, then review it with the user.',
        cautions=cautions or ['This activity is a compact guide to the cited scope, not the complete author curriculum.'],
        variants=[], evidence_status='primary_checked',
        design_basis='Steps/purpose summarize the cited source. Output field schema, execution role, skill idea and any inferred dependencies are our design proposals.'
    ))

def dep(artifact, reason, id=None, hard=True, basis='inferred'):
    return dict(activity_id=id, artifact=artifact, strength='hard' if hard else 'soft', reason=reason, basis=basis)

source('yc-recap-1', 'YC Week 1: Hale and Migicovsky (abridged)', 'https://www.ycombinator.com/blog/startup-school-week-1-recap-kevin-hale-and-eric-migicovsky/', 'Hale 00:43–15:19; Migicovsky 15:19–end.', 'Explicitly shortened lectures; original full videos remain unreviewed.')
activity('PB-001', 'Evaluate a venture-growth hypothesis', 'yc-recap-1', 'prioritize', 'Examine why an idea could grow rapidly.', [
    'Describe problem, proposed solution and explanatory insight.',
    'Consider reach, growth, urgency, cost, necessity and frequency of the problem.',
    'Examine founder, market, product, acquisition and defensibility advantages.',
    'Distinguish basic feasibility from the exceptional claim that would drive growth.'
], ['Growth hypothesis review','problem','solution','insight','advantage claims','evidence gaps'], cautions=['Venture-growth lens; no universal rejection rule for small businesses.'], scope='Hale 02:13–15:09')
activity('PB-002', 'Conduct a recent-behavior customer conversation', 'yc-recap-1', 'discover', 'Understand experienced problems and attempted remedies.', [
    'Discuss the person’s circumstances rather than pitching.',
    'Ask about a recent difficult incident and why it was difficult.',
    'Explore attempted solutions and remaining frustrations.',
    'Listen, record specifics and maintain direct founder contact.',
    'Adapt recruiting and follow-up to idea, prototype or live-product stage.'
], ['Interview record','participant context','incident','attempts','frustrations','follow-up'], inputs=['Learning question','Access to a relevant real participant'], execution='hybrid', dependencies=[dep('Real participant access','An interview record requires an actual conversation.')], scope='Migicovsky 17:36–end')

source('walling-628','Walling: 5PM','https://www.startupsfortherestofus.com/episodes/episode-628-the-5-pm-pre-validation-framework','Framework and two worked examples; sponsorship/social chatter excluded.')
activity('PB-003','Screen an idea with 5PM','walling-628','prioritize','Compare bootstrap-oriented opportunities.',[
    'Check problem importance and urgency; consider alternative ways to solve it.',
    'Identify purchaser, adoption habits, budget and buying context.',
    'Examine subscription fit, charging model and expected account revenue.',
    'Consider market size, competition and reachability.',
    'Check product–founder fit and the effort required to validate.'
],['5PM assessment','six dimensions','supporting evidence','unknowns','comparison rationale'], scope='03:37–end of worked examples', cautions=['A numeric weighted score would be our invention; the source supplies criteria.'])

source('walling-840','Walling: 5PM revisited and founder questions','https://www.startupsfortherestofus.com/episodes/episode-840-5-pm-revisited-starting-over-after-failure-never-shipping-and-more-listener-questions-rob-solo','Framework update and product/business questions; personal recovery narrative is outside product-work scope.')
activity('PB-004','Recheck pricing and market assumptions in context','walling-840','model','Refine an overly generic 5PM assessment.',[
    'Consider pricing against the customer, use pattern and business context.',
    'Check whether the market can support the intended business ambition.',
    'Identify which judgments need experience or further evidence.'
],['Contextual pricing review','customer/use case','business ambition','pricing assumptions','market sufficiency'], inputs=['Customer and business context','Existing or draft pricing/market assumptions'], dependencies=[dep('5PM assessment','Useful starting point, but equivalent assumptions suffice.','PB-003',False)], scope='02:19–07:01')
activity('PB-005','Review shipping and acquisition constraints','walling-840','execute','Identify concrete business bottlenecks.',[
    'Weigh custom internal tooling against growth work and maintenance.',
    'Match acquisition effort to customer economics and awareness.',
    'Reduce repeated launch delays to a concrete release decision.',
    'Consider available validation channels when paid traffic is unsuitable.'
],['Bottleneck review','constraint','candidate action','tradeoff','next check'], scope='07:01–end, excluding personal recovery story', cautions=['Advice is context-bound, especially B2C economics; no blanket prohibition is inferred.'])

source('walling-706','Walling: 2/20/200 and design decisions','https://www.startupsfortherestofus.com/episodes/episode-706-2-20-200-validation-prior-art-and-designing-by-committee-a-rob-solo-adventure','Validation segment and adjacent attribution/decision guidance.')
activity('PB-006','Stage validation effort with 2/20/200','walling-706','experiment','Escalate investment as evidence develops.',[
    'Use a short 5PM screen to compare initial ideas.',
    'Take promising candidates to conversations and/or landing-page tests matching the intended channel.',
    'Consider a usable MVP, including manual or no-code delivery, after that learning.'
],['Staged learning plan','screen','field test','MVP option','decision checkpoints'], execution='hybrid', order='The source proposes progressive stages; the numbers are approximate hours.', independent='A current project may enter at its existing evidence stage after reviewing what has already been learned.', scope='10:27–16:03', cautions=['Hours are rough effort bands, not respondent counts or compulsory budgets; confidence percentages are illustrative.'])
activity('PB-007','Set a small decision group and credit method origins','walling-706','facilitate','Keep decision-making coherent and acknowledge prior work.',[
    'Identify and credit the origin of borrowed frameworks.',
    'Limit design input to people appropriate to the decision.',
    'Use broad feedback selectively rather than giving everyone authorship.'
],['Decision setup','decision owner','contributors','feedback purpose','method attribution'], scope='02:37–10:27 and 16:03–end')

source('nfx-patterns','NFX: five idea patterns','https://www.nfx.com/post/hidden-patterns-great-startup-ideas','All five public frameworks; private extra frameworks unavailable.')
activity('PB-008','Explore five structural idea lenses','nfx-patterns','frame','Examine the opportunity structure behind an idea.',[
    'Separate proven elements from the specific novelty.',
    'Identify recent technological changes enabling a different experience.',
    'Test a non-consensus thesis rather than equating consensus with merit.',
    'Consider both relieving problems and creating desirable possibilities.',
    'Separate market uncertainty from execution uncertainty and assess founder fit.'
],['Structural lens review','novel element','enabling change','contrarian thesis','desired possibility','risk mix'], independent='The five lenses can be applied independently or in parallel to the same idea.', scope='Frameworks 1–5')

source('nfx-pmf-places','Gigi Levy-Weiss: 10 places to find PMF','https://www.nfx.com/post/10-places-to-find-product-market-fit','Ten lenses, brief iteration outline and engagement/retention distinction.')
activity('PB-009','Generate opportunities from ten market patterns','nfx-pmf-places','frame','Find underserved needs or desires.',[
    'Explore much easier or better/networked existing activities.',
    'Look for unused supply, new willingness to pay or disconnected communities.',
    'Consider new earning opportunities or digitizing analog activities.',
    'Explore free pricing, younger audiences for proven products or new sources of enjoyment.',
    'Define a customer/value hypothesis, test an MVP and iterate.',
    'Inspect engagement and retention as well as acquisition.'
],['Opportunity alternatives','pattern','audience','value change','assumption','next observation'], independent='Opportunity patterns are alternatives, not sequential steps.', scope='Ten numbered places and opening/closing PMF guidance', cautions=['The CSV misattributes the author; the page credits Gigi Levy-Weiss. Opportunity patterns do not prove PMF.'])

source('fr-idea-frameworks','First Round: 12 idea-finding frameworks','https://review.firstround.com/12-frameworks-for-finding-startup-ideas-advice-for-future-founders/','All twelve numbered sections; linked full contributor methods not acquired here.')
activity('PB-010','Choose among twelve idea-development approaches','fr-idea-frameworks','frame','Use complementary approaches to find and sharpen ideas.',[
    'Invest in choosing the problem.', 'Prepare through immersion and invite challenges.',
    'Connect large problems, personal advantages and a business possibility.',
    'Inspect changing, apparently crowded or overlooked markets.', 'Relax plausible constraints.',
    'Timebox a shared project to explore idea and cofounder fit.', 'Let a clear problem thesis develop.',
    'Describe customer jobs and compare unmet importance.', 'State a specific vision, advantage and timing.',
    'Review functional need, emotional need, market and experience.',
    'Pitch, record feedback and revise selectively.', 'Check enduring personal motivation.'
],['Idea exploration menu','chosen lens','candidate ideas','learning artifact','fit rationale'], order='Article groups approaches by exploration context; it does not require all twelve.', independent='Choose any relevant lens; cofounder and idea exploration can run together.', scope='Numbered sections 1–12', cautions=['The menu is compact; examples and linked full procedures require their own sources.'])

source('mom-teachers','Fitzpatrick: teacher activity overview','https://www.momtestbook.com/teachers','Four named activity types; chapter references only.', 'Full book examples/instructions absent. Steps below map activity types; facilitation specifics are proposals.')
activity('PB-011','Practice customer-conversation skills','mom-teachers','discover','Prepare for less misleading interviews.',[
    'Practice rewriting weak questions.', 'Identify major risks and three learning goals.',
    'Plan appropriate commitments for meetings.', 'Rehearse with mock conversations.'
],['Interview preparation pack','revised prompts','learning goals','commitment options','rehearsal notes'], execution='team_workshop', independent='These four activities can run separately; use rehearsal before real conversations when useful.', scope='Recommended teaching topics', cautions=['Official page names activities but does not expose full book exercises. A simulated respondent is practice, never customer evidence.'])

source('mellinger-discovery','Mellinger: early customer discovery','https://review.firstround.com/how-to-know-if-your-ideas-the-right-one-a-founders-guide-for-successful-early-stage-customer-discovery/','Three phases and their substantive subheadings.')
activity('PB-012','Plan a focused research sprint','mellinger-discovery','discover','Make the next research decision explicit.',[
    'Choose the next decision and one or two learning questions.',
    'Narrow the audience by behavior and relevant demographics.',
    'Recruit a small focused batch; examine distinct groups separately.'
],['Research plan','decision','learning questions','audience criteria','recruitment batch'], scope='Phase 1')
activity('PB-013','Interview from broad context to specifics and back','mellinger-discovery','discover','Collect useful accounts while checking bias.',[
    'Begin with broad context, explore specifics, then revisit wider priorities.',
    'Avoid leading wording and premature product disclosure.',
    'Ask about past behavior; use short questions and follow-ups.'
],['Conversation notes','context','reported behavior','counterevidence','follow-ups'], inputs=['Research focus','Real participant'], execution='hybrid', dependencies=[dep('Research focus','Focus guides questions.','PB-012',False),dep('Real participant','Actual accounts cannot be simulated.')], scope='Phase 2', cautions=['An elicited price reaction is not a purchase commitment.'])
activity('PB-014','Synthesize interviews at three cadences','mellinger-discovery','measure','Move from observations to patterns and actions.',[
    'Keep records of supporting and conflicting data and strong reactions.',
    'Debrief each interview into data, interpretation and action.',
    'Review findings weekly and use broader affinity grouping when needed.'
],['Research synthesis','observation links','themes','counterexamples','actions'], inputs=['Real interview notes'], execution='ai_draft', dependencies=[dep('Interview notes','Synthesis needs source observations.','PB-013')], independent='Can analyze any suitable existing notes; longer synthesis need not await a fixed number of sessions.', scope='Phase 3', cautions=['The article gives differing short-debrief durations; preserve the purpose rather than a universal timer.'])

source('fr-validation-tactics','First Round: seven validation tactics','https://review.firstround.com/unconventional-tactics-for-validating-your-startup-idea/','Seven tactic sections; underlying cases are context-specific.')
activity('PB-015','Select a conditional validation tactic','fr-validation-tactics','experiment','Expand the ways to learn about a proposal.',[
    'Test a small unit of value.', 'Explore selling before a product exists.',
    'Observe relevant workplace problems.', 'Seek reactions outside friendly social circles.',
    'Consult industry insiders.', 'Interview skeptics and adoption gatekeepers.',
    'Compare ideas with founders without signaling a favorite.'
],['Tactic selection','uncertainty','audience','chosen tactic','observed signal'], execution='hybrid', independent='Seven alternative tactics, not required predecessors for each other.', scope='Seven tactic subheadings', cautions=['Keep recruiting transparent; no invented sales, misleading product availability or unapproved outreach is implied. Founder excitement differs from customer behavior.'])

source('biyani-mvt','Biyani: Minimum Viable Testing','https://review.firstround.com/the-minimum-viable-testing-process-for-evaluating-startup-ideas/','Three-step method, cases, next paths and limitations.')
activity('PB-016','Design a Minimum Viable Test','biyani-mvt','experiment','Test one essential assumption with the smallest useful unit.',[
    'Clarify the customer promise from current behavior.',
    'List demand, execution, marketing, market-size and profit risks.',
    'Choose one primary uncertainty and a narrow unit of value.',
    'Deliver or simulate only what that test requires; observe actual action.',
    'Review remaining risks and choose another test, product work or stopping.',
    'Keep one-off test revenue distinct from sustainable growth.'
],['MVT brief and result','value promise','primary risk','unit of value','measurement','result','next decision'], inputs=['Candidate promise','Relevant audience'], execution='hybrid', dependencies=[dep('Primary uncertainty','The test scope must be tied to a question.')], independent='Run when a risky claim is identifiable. Other MVTs may run in parallel if results and exposures can be separated.', scope='Three-step process; What comes next; Closing thoughts')

source('stanford-llp','Stanford: Lean LaunchPad course requirements','https://leanlaunchpad.stanford.edu/course-info','How You’ll Learn, Projects, Deliverables; administrative requirements excluded.', 'Public course brief, not all assigned readings, lectures or a complete course curriculum.')
activity('PB-017','Run a weekly business-model learning cycle','stanford-llp','facilitate','Test a business model through repeated fieldwork.',[
    'Prepare hypotheses and contacts around a model area.',
    'Conduct customer fieldwork and revise the concept from learning.',
    'Present weekly learning, discuss critiques and record lessons.',
    'Produce an appropriate real prototype/product; physical products include costed materials.'
],['Weekly learning review','model area','hypotheses','contacts','observations','changes','product evidence'], execution='hybrid', order='Repeated course cadence; stated interview loads belong to that course.', independent='Can be adapted around any current model uncertainty; not a prerequisite for individual catalog exercises.', scope='How You’ll Learn; Projects; Deliverables')

source('maurya-fill-order','Maurya: Lean Canvas fill order','https://medium.leanstack.com/what-is-the-right-fill-order-for-a-lean-canvas-f8071d0c6c8c','Entire methodological argument and three deconstruction steps.', 'Article only, not Running Lean book or full Lean Canvas workbook.')
activity('PB-018','Snapshot an idea and inspect its chain of beliefs','maurya-fill-order','model','Make the origin and uncertainty of a model visible.',[
    'Start from the idea’s real backstory; sketch a quick canvas, allowing blanks.',
    'Examine the first boxes filled and how they constrain later beliefs.',
    'Distinguish intuition, anecdote and empirical support.',
    'Review customer, market and technical risks; learn about the weakest important links.'
],['Canvas and belief audit','idea trigger','canvas boxes','belief sequence','support type','learning priorities'], order='No universal canvas fill order; testing order depends on risk.', independent='May begin with a solution, customer, invention or constraint. Revisit after any major new evidence.', scope='How to Deconstruct an Idea', cautions=['Do not fabricate customer/problem boxes to justify a favored solution.'])

source('aulet-interview','Aulet: entrepreneurship interview (MIT-linked)','https://hbr.org/podcast/2024/09/24-steps-to-launch-a-start-up','Interview framing only.', 'Interview explicitly does not cover all 24 steps. No detailed DE exercises reconstructed from it.')
coverage.append(dict(source_id='aulet-interview', section='Whole available interview', status='bounded_overview', activity_ids=[], notes='The overview is a resource lead; the 24-step book needs independent procedure/worksheet coverage.'))

source('torres-ost','Torres: Opportunity Solution Trees','https://www.producttalk.org/opportunity-solution-trees/','Public guide: prerequisites, outcome, opportunity mapping, selection, solutions and iteration.', 'Book and linked courses not reviewed; guide itself supplies usable bounded guidance.')
activity('PB-019','Build and revise an Opportunity Solution Tree','torres-ost','discover','Connect an outcome to evidenced opportunities and alternatives.',[
    'Start with a customer/value theory, outcome and several real customer stories.',
    'Map experiences and group unmet needs into opportunity branches.',
    'Separate needs from solutions; compare importance and strategic fit.',
    'Choose a small opportunity and explore alternative solutions.',
    'Link assumption tests; refine the tree as interviews continue.'
],['Opportunity tree','outcome','story-linked needs','branches','target opportunity','solutions','tests'], inputs=['Outcome','Target customer/value hypothesis','Customer stories'], execution='hybrid', dependencies=[dep('Customer stories','The source requires story-grounded opportunities.',None,True,'source'),dep('Outcome','The tree is organized toward an outcome.',None,True,'source')], independent='Can start from existing suitable interviews; does not require a Foundation Sprint first.', scope='Prerequisites through solution selection', cautions=['Fictional profile details are not valid evidence for opportunity branches.'])

source('torres-assumptions','Torres: Assumption Testing','https://www.producttalk.org/assumption-testing/','Public assumption discovery, mapping, tests, evaluation and decisions.')
activity('PB-020','Compare solutions through assumption tests','torres-assumptions','experiment','Learn about risky parts before committing to a whole solution.',[
    'Walk through alternative experiences and expose their assumptions.',
    'Consider desirability, viability, feasibility, usability and ethical uncertainties.',
    'Prioritize important claims with weak support.',
    'Define success before selecting and running a small test.',
    'Evaluate patterns across tests and revise the alternatives or opportunity.'
],['Alternative-assumption comparison','solutions','assumptions','priority','test criteria','results','decision'], inputs=['Candidate solutions','Current evidence'], execution='hybrid', dependencies=[dep('Candidate solutions','Specific solution assumptions require a proposed experience.'),dep('Opportunity tree','Helpful context, not required to test an already defined assumption.','PB-019',False)], scope='Identify assumptions; prioritize; evaluate tests', cautions=['Small discovery tests are not necessarily controlled experiments or conclusive validation.'])

source('cagan-risks','Cagan: Four Big Risks','https://www.svpg.com/four-big-risks/','Full article.')
activity('PB-021','Separate four product risks','cagan-risks','prioritize','Avoid using one kind of evidence to answer a different risk.',[
    'Check whether people will choose or buy the product.', 'Check whether intended users can use it.',
    'Check technical delivery feasibility.', 'Check whether it works within the business.',
    'Involve product, design and engineering in the appropriate questions.'
],['Risk register','value','usability','feasibility','viability','owner','evidence','next check'], scope='The four risks and team responsibilities', cautions=['No source numeric ranking or pass threshold.'])

source('cagan-build','Cagan: Build to Learn vs Build to Earn','https://www.svpg.com/build-to-learn-vs-build-to-earn/','Concept article; FAQ is a linked expansion.')
activity('PB-022','Choose learning or delivery requirements for a build','cagan-build','design','Match engineering effort to the purpose of the artifact.',[
    'State which uncertainty a learning prototype addresses.',
    'Distinguish temporary learning needs from production obligations.',
    'Continue discovery alongside delivery as new risks emerge.'
],['Build-purpose brief','learning question','prototype scope','production obligations','next evidence'], scope='Full concept article', cautions=['A conceptual distinction; this brief format is our adaptation. A prototype does not establish all four risks.'])

source('dunford-positioning','Dunford: positioning quickstart','https://www.aprildunford.com/post/a-quickstart-guide-to-positioning','Five components, dependency argument and two common mistakes.')
activity('PB-023','Develop positioning from real customer alternatives','dunford-positioning','position','Make differentiated value clear to the right customers.',[
    'Identify what customers would do without the product, including the status quo.',
    'List capabilities those alternatives lack.',
    'Translate capabilities into customer value.',
    'Identify customers who care most about that value.',
    'Choose a market context that makes the value understandable.'
],['Positioning brief','actual alternatives','distinct capabilities','value','best-fit characteristics','category'], inputs=['Product capabilities','Customer alternatives'], dependencies=[dep('Customer alternatives','The source derives differentiation from the actual comparison set.',None,True,'source')], order='Alternatives → capabilities → value → best-fit customers → category in this method.', independent='A standalone positioning exercise once a comparison set exists; the customer profile can be revised here even if one was drafted earlier.', scope='Customer-Centric Methodology; Common Mistakes', cautions=['A web competitor list alone is not the customer’s real alternatives. Choosing a category differs from writing messaging.'])

source('yc-recap-2','YC Week 2: Seibel MVP lesson (abridged)','https://www.ycombinator.com/blog/startup-school-week-2-recap-michael-seibel-adora-cheung-and-ilya-volodarsky/','Seibel 00:43–10:12 only.', 'Shortened official lesson. Adjacent KPI/analytics lectures are not silently included as the requested MVP resource.')
activity('PB-024','Write and cut an MVP specification','yc-recap-2','execute','Put a useful initial version in front of a narrow first audience.',[
    'Choose initial users and their highest-priority problem.',
    'Write a timeboxed specification with very limited functionality.',
    'Cut scope when the date is threatened.',
    'Get users interacting, gather feedback and iterate on the solution.',
    'For long technical development, consider a simple explanatory starting artifact.'
],['MVP scope','first users','core problem','included features','deferred features','release target','feedback loop'], inputs=['Initial audience and problem','Delivery constraints'], execution='hybrid', order='Scope → build/release → observe → iterate; no fixed prior workshop.', independent='Can use existing customer/problem work. A product experiment and a production MVP have different completion criteria.', scope='Seibel 00:43–10:12', cautions=['Release speed does not waive real operational or regulatory requirements.'])

source('vohra-pmf','Vohra: Superhuman PMF engine','https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/','Survey eligibility, four-step engine and iteration.', 'First-person case method; benchmark and roadmap split are not universal guarantees.')
activity('PB-025','Survey experienced users and find strong-fit segments','vohra-pmf','measure','Locate groups that strongly value an existing product.',[
    'Survey users who recently experienced the core product.',
    'Ask about losing access, likely beneficiaries, main benefit and improvements.',
    'Analyze disappointment by segment and characterize strongest-fit users.'
],['PMF segment analysis','eligibility','denominators','responses','segment definitions','valued benefit'], inputs=['Product in use','Eligible real users and survey responses'], execution='hybrid', dependencies=[dep('Actual product experience','A raw idea or fictional persona cannot answer this survey.',None,True,'source')], scope='Anchoring metric and step 1', cautions=['The reported 40% benchmark is a diagnostic, not proof of success.'])
activity('PB-026','Turn segmented PMF feedback into a roadmap','vohra-pmf','decide','Use benefit-aligned feedback to guide improvements.',[
    'Identify what committed users value and what holds similar users back.',
    'Prioritize strengthening the core benefit and removing relevant barriers.',
    'Repeat measurement and revise priorities.'
],['PMF-informed roadmap','valued themes','barriers','segment rationale','work choices','repeat measurement'], inputs=['Segmented survey results'], execution='ai_draft', dependencies=[dep('Segmented survey results','The feedback policy depends on who values which benefit.','PB-025')], scope='Steps 2–4', cautions=['Do not turn the case’s selective feedback policy into a rule to ignore all dissatisfied users.'])

source('fr-measure-pmf','First Round: measuring PMF','https://review.firstround.com/how-to-measure-product-market-fit/','Thesis, validation, MVP, survey and primary-metric sections.')
activity('PB-027','Choose a product-value metric and supporting measures','fr-measure-pmf','measure','Keep product learning tied to meaningful usage.',[
    'Start with a customer/problem thesis and test a focused product.',
    'Use product-experience feedback to investigate fit.',
    'Select a primary metric relevant to value and track useful supporting measures.',
    'Distinguish impressive totals from operational signals.'
],['Measurement plan','primary value metric','definition','supporting metrics','audience','review cadence'], inputs=['Product stage and intended value'], independent='Can be drafted early; actual PMF measurement requires experienced users.', scope='How to find PMF; How to measure PMF', cautions=['The article’s metric menu is not a prescription to track every metric or treat market size as a usage outcome.'])

source('fr-pmf-paths','First Round: 20 paths to PMF','https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/','Twenty numbered lessons; detailed per-case extraction is still pending.', 'Do not label complete until all twenty numbered sections are explicitly mapped.')
coverage.append(dict(source_id='fr-pmf-paths', section='20 numbered lessons', status='pending_mapping', activity_ids=[], notes='Article accessed; final catalog must account for every numbered lesson, including beginning/end sections not yet mapped.'))

for s in sources:
    ids=[a['id'] for a in activities if a['source_id']==s['id']]
    if ids:
        coverage.append(dict(source_id=s['id'], section=s['coverage'], status='bounded_procedure_mapped', activity_ids=ids, notes=s['limitations'][0]))

if __name__ == '__main__':
    out=dict(sources=sources, activities=activities, coverage=coverage)
    (ROOT/'data/public-activities.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Wrote {len(sources)} public source records and {len(activities)} activities; pending coverage remains explicit.')
