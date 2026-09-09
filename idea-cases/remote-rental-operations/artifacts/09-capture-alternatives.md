# Capture readiness evidence with less interruption

2026-09-09 · A12 · Scope revision 3 · Research and concept sketches, not an implemented feature

## The current explanation is plausible, not verified

Brandon explicitly labels his explanation speculative. His description supplies concrete things to inspect: repeated phone handling, searching a long room-by-room form, ambiguous required/optional sections, identifying the correct room, invoking the camera and finding the save action. Cleaning reportedly fits the cleaner's familiar routine of working while using the phone for listening/talking. She is described as in her fifties, with an ordinary phone of unspecified model.

The app already has minimum-photo requirements; it does not require every possible photo. The family already tried grouping cleaning, inventory, problems and saving. Brandon thinks that helped somewhat but did not make the process easy. Neither fewer mandatory items nor section grouping should be presented as an entirely new discovery.

E48 remains the report that she stopped using completion features. This latest account offers possible causes; it is not a direct cleaner interview, observed usability study or proof that photographs themselves are unacceptable. Physical interruption and software navigation are separate sources of effort. A smoother camera interface could still fail if the capture workload is too large.

The underlying need is usable readiness evidence for the owner at acceptable effort for the person on site. This applies Pincus's need/implementation separation and informs Knapp–Zeratsky's comparison of approaches. It is not a commitment to a full new product.

## What current technology offers

Official sources reviewed 2026-09-09; vendor claims are not independently measured outcomes.

| Approach | Supported capability or proposed mechanism | Practical limit for this case |
| --- | --- | --- |
| Guided still photos | Properly documents reference photos, matching viewpoints and live verification capture. A camera sequence can associate a shot with the requested view without making the cleaner hunt through form fields. | Guidance can still be burdensome. A frame can miss dirt, stock or context; it does not prove all work or later condition. [Properly documentation](https://help.getproperly.com/en/articles/5470548-take-verification-photos) |
| Photos with optional spoken notes | CompanyCam documents a Walkthrough Note assembled while taking photos and speaking; its glossary explicitly distinguishes this from video. | Adjacent contractor product, not evidence that this cleaner would adopt it. Voice recognition and the fit with her listening routine need testing. [CompanyCam glossary](https://help.companycam.com/en/articles/15946673-companycam-glossary) |
| Simple job-specific photo inbox | CompanyCam documents capturing/uploading photos inside a selected project. Its guest-access flow accepts photos and notes through a link but includes identity verification. | A relevant interaction pattern, not a zero-friction or accountless guarantee. Organizing unlabelled pictures can move work to the reviewer. [Project capture](https://help.companycam.com/en/articles/14808615-getting-started-with-companycam), [guest access](https://help.companycam.com/en/articles/6828446-using-companycam-with-guest-access) |
| One short video pass | Proposed alternative: capture a continuous route and review/extract useful frames afterward. | No evaluated implementation in this study. Movement, missed close-ups, sound, upload/review effort and the actual phone may make it worse than selected photos. Do not call CompanyCam's Walkthrough Note video. |
| LiDAR/3D scan | Apple's RoomPlan uses camera/LiDAR input to represent room dimensions and recognized furniture. | Requires compatible hardware; this phone is unverified. Geometry is not evidence that linens changed, towels are sufficient or surfaces are spotless. [Apple RoomPlan](https://developer.apple.com/augmented-reality/roomplan/) |
| Targeted device readings | Earlier A08 covers supported temperature, connectivity and battery readings. | These can answer particular equipment questions, not certify overall cleaning. Air-particle measurements also cannot establish furniture arrangement or stock. See [A08](07-readiness-technology.md). |

The reviewed sources do not establish a replacement sensor that certifies all of Mom's standards with less effort. They do show alternative ways to collect and organize evidence. The comparison is bounded; it is not an exhaustive claim that no other technology exists.

## Recommended first concept: one final capture session

**Goal:** let an experienced cleaner finish their normal routine, then capture the agreed evidence in one short pass. This could reduce repeated phone handling and form navigation. It could also add an extra walk, so the net benefit is an untested hypothesis.

This is a screen-by-screen concept for the existing app, not a prototype or a new family assignment. Labels and examples are illustrative; no fixed photo count has been selected.

| Step | Cleaner sees/does | Work the app should take on |
| --- | --- | --- |
| 1. Start final photos | The current property/job and one obvious primary action: **Start final photos**. Guidance remains available when needed. | Carry the job context forward so she does not select it for every photo. |
| 2. Capture in sequence | A camera view and one clear reference: for example, the agreed view of the bed or shower. Capture advances to the next requested view; back/retake remains available. | Associate the shot with that requested view, save without a separate form-submit hunt, and show clear progress. Do not infer she is in the right room solely from the screen label. |
| 3. Report exceptions | A brief final opportunity to report a shortage, damage or an unavailable view. Optional voice can supplement text/photos. | Keep routinely required evidence distinct from issue reporting. Do not treat silence as proof that no shortage or fault exists. |
| 4. Send and see receipt | A short summary of what is included or unresolved, one send action and a clear received/pending state. | Separate photos saved on the device, successfully delivered report, owner review and payment. Upload failure must not masquerade as a report received. |

Select requested views by the readiness decisions they support, together with Mom and the cleaner; do not assume an arbitrary smaller set is sufficient. Missing critical evidence should remain explicit. An owner-facing report should show what is covered and unknown, not declare the house perfect.

Grouping sections remains useful for finding guidance, but this concept changes the capture interaction itself. It removes repeated form location and save decisions from the proposed photo path. A paid cleaning job's substantive scope is unchanged by a nicer reporting interface.

## Alternative worth preserving: take photos freely, organize afterward

One job-specific camera/inbox lets her take the agreed pictures in her own order. The app could propose room labels or identify a missing requested view afterward. AI sorting is a candidate, not a verified capability of the family app; similar bedrooms, framing and low-quality images can create ambiguity. A plain reviewable inbox can be compared before adding automatic classification.

The guided route reduces classification ambiguity but constrains order. Free capture gives the cleaner more control but risks missed views and additional reviewer work. Neither is established as better for this cleaner. An eventual comparison should hold the requested evidence approximately constant so a reduction in proof is not mistaken for an improvement in interaction.

## Design constraints and unresolved questions

- Design around the actual phone, connection and routine. Age alone is not a diagnosis, and the stated 99.9% smartphone figure is not established evidence. The current cleaner reportedly has a phone; wider provider/device coverage remains unknown.
- AI could assist with organization, blur/coverage flags and notes. Keep uncertain outputs reviewable; photos, classifications and notes do not establish hidden cleanliness or automatic payment eligibility. Accuracy and cost remain untested.
- The property standards should make required evidence clear. We still need to distinguish presentation, actual cleaning, supplies and device status; each may need different evidence.
- Asking the primary cleaner to find substitutes is a separate proposed coordination responsibility. It requires agreement, practical authority and clarity on compensation; it does not remove the work or establish available coverage. No such arrangement was made here.

## Handoff

The prior live tests and recording sheet remain on hold. The immediate user task is a founder review of the four-step concept: **which step, if any, still seems likely to annoy or interrupt her?** This is a reaction to a specific proposed flow, not a new incident questionnaire or evidence that the cleaner would use it.

The facilitator then refines the smallest screen walkthrough worth showing. An actual cleaner usability observation is still needed before concluding that the flow helps; independent host demand, support economics and business viability remain unvalidated.
