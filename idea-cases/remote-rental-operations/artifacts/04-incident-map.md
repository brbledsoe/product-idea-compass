# Reported incidents, attempted solutions, and unresolved work

2026-09-06. Scope revision 2. Session 2 snapshot; [session 3 analysis](05-readiness-and-response.md) supplies the later recurrence estimates and current next question.

Question: which recurring operational problem deserves the next test?

Method: incident-grounded Knapp–Zeratsky Foundation Basics and Pincus component/variant separation, using the saved sources already reviewed in session 1. This is a synthesis of Brandon's report, not an independent customer study or technical diagnosis.

## What is now known

Brandon described local family management in Texas while other family members are overseas and asleep during some guest interactions. Municipality and initial sales market remain unknown. The current app exposes cleaning opportunities, supports cleaner sign-ins and access-related flows, and uses task lists/photos in a workflow tied to payment. The family connected an alarm through Home Assistant into its app. These are reported capabilities, not inspected implementation.

The user favors a software/automation business and does not want a staffed cleaning business. Independent owner buyers, local manager buyers, and a provider-network model remain open; he currently prefers the owner-facing ambition. Describing the target as older hosts still has no supporting host-age evidence. Older guests experienced the lockout; this is a different audience.

## Incident and solution map

| ID | Reported problem and consequence | Current solution/workaround | Friction introduced or left unresolved | Provisional significance |
|---|---|---|---|---|
| INC-01 | Primary cleaner saw an upcoming job in the app but was going out of town. A cleaning deadline created pressure to find coverage. | Cleaner contacted Brandon's mom; family asked for referrals; cleaner contacted her network and found a substitute. | Unpaid referral/coordination work, uncertain availability/trust/price, and no confirmed backup until people finished calling. | High operational urgency; one absence episode with several substitute visits, not several independently observed sourcing failures. |
| INC-02 | Substitute needed to enter and complete the house's work/payment flow. | Family created a temporary sign-in and substitute installed the app. | Setup and navigation were difficult for a short engagement. Cleaner needed to learn a workflow to do an already-understood job. | Candidate product test: reduce onboarding and handoff burden; customer preference and existing competitor gap unproven. |
| INC-03 | Family wanted assurance that rooms, supplies and damage checks met its standards. | Checklists and photos required before payment. | More checks burden cleaners and feel intrusive; fewer checks reduce owner confidence. Owner still needs to interpret evidence. | Recurring readiness workflow, but hours, actual completion rates, false alarms and defect rates are unknown. |
| INC-04 | Storm/power interruption preceded lost alarm integration/connection. Guests had valued the alarm option. | Back-and-forth troubleshooting and calls; mom went to the property. | Unclear failure location and whether remote recovery was possible; no trusted/cost-predictable local technical help. | Remote recovery problem. ADT identity, root cause, affected integration, restored state and elapsed time are uncertain. |
| INC-05 | Guest door code failed; an older couple waited in the heat and contacted the host while remote replies were delayed. | Mom attended and shared her personal code. Low battery was subsequently noticed; Brandon suspects a loss of app connection. | Failure discovered by guests, dependency on a local person, unknown battery-alert capability, and reliance on another code. | Highest immediate guest impact in the account. Low battery is reported, but its causal role and chronology are not established; another code does not prove recovery from a dead battery. |
| INC-06 | Guests repeatedly requested more towels for a week-long stay. Washer/dryer also broke. | Guest messaging; family considered cleaner restocking and how to represent broken/restored amenities. | Supply planning and property readiness uncertain; reporting/repair/listing/guest notification are separate steps. | Concrete guest-experience failure; do not assume towel shortfall was caused by the cleaner or washer failure without evidence. |
| INC-07 | Family lacks a trusted repair network and fears an expensive call-out for a simple fix. | Mom and family coordinate calls or visits. | Diagnostics, vendor selection, cost approval and follow-through remain manual. | Cross-cutting capacity and trust problem. No actual quote, repair invoice or overcharge was reported. |

All incidents are participant-reported from one family/property context. Exact dates, counts, total labor, cost and independently verified outcomes are missing. Cleaner-replacement work reportedly succeeded for a few visits until the primary returned; this does not establish reliable autonomous fulfillment.

## Interpretation: what is most consequential versus most promising to test

The common problem appears to be getting reliable confirmation that a distant property is ready and recovering quickly when it is not. Mom supplies much of the missing coordination and local judgment. This is a provisional problem statement, not a selected product.

1. **Guest access failure has the strongest immediate severity evidence.** It interrupted entry and required a local response. Frequency and whether existing supported locks/monitoring could solve it are unknown.
2. **Cleaning coverage and substitute onboarding are the clearest described coordination chain.** There is a concrete current workaround and access to the original cleaner, replacement workflow and family coordinator. A smaller test could compare a job-specific invitation/guide with the present app, but do not assume an app-free link beats current tools or solves local provider supply.
3. **Readiness checks/restocking have repeated workflow exposure.** They link owner confidence to cleaner workload. The goal is sufficient reliable evidence at acceptable effort; automatic certification from arbitrary photos is not established.
4. **Alarm and appliance recovery matter but span heterogeneous hardware and local services.** A broad promise across device types could introduce substantial support burden. Root causes have not been diagnosed.

These are qualitative judgments about this account. They are not a scored market ranking. Frequency and total owner/provider effort must guide which problem becomes the first investment.

## Candidate solutions, explicitly not validated

- Owner-approved referral invitations for a specific job, so a primary cleaner can suggest a substitute without creating an open marketplace. Invite, accept, access, work guide, exceptions, evidence and completion are distinct moments to test.
- A short property-specific job page with only the necessary instructions and a small set of evidence requests. Compare task completion and assistance needed with the existing sign-in/app flow. Any access mechanism needs suitable permissions; no credentials are stored in these artifacts.
- Pre-arrival readiness checks for supported devices and critical supplies, with a named recovery route. Monitoring alone has value only if someone can act in time. Battery warnings/connection status depend on actual devices and integration support.
- Photos can support visible-condition review. They cannot establish unseen conditions, smells or everything outside the frame. AI accuracy, ambiguous cases and effort saved need testing against actual inspection evidence; neither completed checkboxes nor selected photos guarantee the whole house meets every standard.
- Track an amenity as reported unavailable, under repair, and confirmed restored, with separate actions for listing information and affected reservations. No production state model or integration has been specified.

## Additional ideas retained, with weaker evidence so far

| Component | Underlying need | Evidence state / unresolved premise |
|---|---|---|
| More candid guest feedback | Learn small improvements guests do not mention spontaneously | Founder perception; no structured guest feedback comparison or proof of suppressed feedback yet |
| TV/local-events guide | Help guests discover nearby places and events | Opportunity hypothesis; no observed usage, demand or verified city API availability |
| Repeat-guest/direct booking | Reduce repeat-stay acquisition/distribution cost and offer a discount | Proposed concept, not reported operation; fee/discount economics and booking-source rules not established |

Keep these in the case while prioritizing operational failures. They are not rejected merely because they are outside the next test.

## Business configuration

Owner-facing software for rental operations can serve a business buyer even when the buyer is an individual. The useful distinction is who buys, who uses the workflow, and who responds to failures. A professional-manager buyer is another possible route, not a required conclusion.

An independent provider marketplace would not require employing all cleaners, but would still need reliable local supply, trust, accepted jobs and a response when jobs fail. A private referral network is a smaller variant to examine before promising a broad Fiverr-like marketplace. Neither model removes the work of establishing standards and responsibility.

## Platform checks relevant to the proposed features

Official pages retrieved 2026-09-06. These are platform rules and instructions, not a legal opinion or exhaustive product compliance review.

- Airbnb's [off-platform policy](https://www.airbnb.com/help/article/2799) prohibits encouraging future/repeat bookings off Airbnb and offering discounts for doing so. It also restricts marketing use of guest contact information and off-platform surveys about Airbnb stays, with stated exceptions. The proposed Wi-Fi-email-to-discounted-repeat-booking funnel conflicts with these restrictions as described. A disclosed purpose does not itself resolve them. Keep any independently acquired direct-booking proposition separate and assess its actual acquisition route before pursuing it. This page also says guest entry must be possible without a required separate account/app, subject to exceptions; cleaner access is not the guest-entry rule's subject.
- Airbnb's [listing-update guidance](https://www.airbnb.com/help/article/1506) says pending/confirmed guests will not see changes to the listing and directs hosts to message upcoming guests immediately about a removed amenity they expected. Updating the listing alone does not close the guest-communication task.
- Airbnb's [privacy standards](https://www.airbnb.com/help/article/3060) prohibit indoor monitoring cameras. The user already rejected indoor cameras; no such system is proposed here.

## Next action

Owner: Brandon supplies a rough recent frequency/burden comparison; facilitator narrows the first test.

Question: Over the last three months, which created the most total work for the family: finding/onboarding substitute cleaners, checking cleaning/supplies, or fixing access/device problems? Rough counts or hours are enough; unknown is acceptable.

Deliverable: a first problem to investigate, chosen using actual burden alongside severity, with the other problems retained.

Completion check: one period and comparative frequency/effort are recorded, or missing data is explicitly identified and a small collection task chosen. Resume when Brandon answers. No new app, provider hiring or customer outreach is required now.
