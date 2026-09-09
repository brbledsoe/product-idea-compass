# Actual app baseline and camera-assisted readiness

2026-09-09 · Mentor-room scope revision 3 · A13

## Main findings

- BookedTexas already contains a broad property-operations application, including finance and image-capable AI chat. Future comparisons should start from this implementation.
- Cleaner photos still attach to individual checklist items. A free-order, job-level photo session and automatic room grouping would be new workflows.
- A final camera pass that suggests visible staging corrections is worth investigating. Its accuracy, effort and effect on Mom's walkthroughs remain untested.
- A property-owned device could standardize the experience independently of LiDAR. RoomPlan specifically requires compatible Apple hardware and native integration.
- A finance aggregation inconsistency was reproduced using synthetic data. The existing dashboard should not yet be treated as a verified answer to property profitability.

## What was inspected

Repository: `C:/Users/Brandon/Documents/Projects/airbnb`, branch `main`, commit `c2ba5ccddb3034617f5dc6562a2e546e0a17ece2`. Working tree was clean at inspection. Static review covered the frontend routes/views, API handlers, database schema/migrations, cron and notification paths, AI assistant, upload paths and PWA configuration.

This establishes code presence and selected control flow. It does not establish which version is deployed, which integrations are configured, whether jobs run reliably, which screens the cleaner sees, or continued adoption. No app source was changed, no live credentials or business records were inspected, and no app build, deployment or live workflow was run. The finance probe below used only an isolated in-memory database.

The application uses Vue 3/TypeScript/Vite, a custom PHP API and a MySQL-style schema. It is an installable web app/PWA; no native RoomPlan implementation was found. Its service worker caches the application shell; that is not evidence of an offline photo-upload queue.

## Capability rundown

| Area | Present in reviewed code | Boundary relevant to the idea |
| --- | --- | --- |
| Properties and people | Multiple properties, assignees, roles/permissions, profiles, language preferences, property operations notes/wiki | Availability of contacts or notes does not establish a vetted provider network or backup owner. |
| Calendar and stays | Airbnb iCal import, booking views, reservation links, local booking overrides, checklist scheduling windows | The reviewed integration imports calendar data. Local overrides do not establish changes to the actual Airbnb reservation, listing, price or guest payment. |
| Cleaning | Configurable task lists, grouped checkboxes, completion/issues, low-stock reporting, per-item attachments, draft save, submission, reopening before payout approval | Checklist lifecycle is open/submitted; I did not find a dedicated accept/decline/backup-dispatch lifecycle. |
| Recurring work | Booking-created/check-in/check-out rules, offsets, monthly checklist rules; standalone daily/weekly/monthly/one-time automation actions | Weekly trash reminders/todos could fit existing scheduling machinery, but somebody still must own the task. |
| Notifications | Email, WhatsApp and Firebase push code; queue/retry and cron records; inbound WhatsApp relayed to admins | Notification delivery is not acceptance. Inbound forwarding is not a complete shared guest conversation workflow. Configuration and live delivery remain unverified. |
| Inventory | Fixed assets/consumables, stock events, condition, low-stock flags, pictures and positions on an uploaded floorplan | Useful property knowledge; the floorplan is an uploaded image with pins, not an automatically scanned 3D room. |
| Finance | Income/expense ledger, receipts, reimbursement review, monthly/all-time totals, property breakdown, forecasts, checklist compensation, monthly payroll and percentage-share configuration | Payout approval creates records; no bank transfer or bill-payment gateway was found. Income/expense completeness remains unknown. An `airbnb_ical` source label/import counter alone does not demonstrate a working income importer. |
| AI assistance | Image attachment, optional browser speech dictation, permission-checked read/write tools for app records, property/wiki/inventory lookup, bill-photo prefill | Generic image chat is implemented. Automatic room labels, staging comparison, continuous scanning and readiness certification were not found. |
| Home automation | Property Home Assistant dashboard link and configurable outbound webhook actions | Actual lock/alarm logic may live in Home Assistant or remote configuration. Native device-health, battery alerts and recovery behavior were not established by this checkout. |

Other supporting code includes password reset/session management, notification settings, bug reporting/MCP tooling, schema migrations and deployment utilities. These were inventoried, not comprehensively security- or reliability-audited.

## The cleaner's current flow, with important corrections

The current view already includes compact task cards, grouped checkboxes, an attention-only filter, expandable problem reporting and low-stock-only inventory reporting. This may reflect revisions after the older long form Brandon described. Source inspection cannot establish which version the cleaner abandoned or whether the current layout is usable for her.

The photo control selects one file at a time, and the upload handler requires a checklist item ID. It uploads immediately and associates the result with that row. It does not provide a job-level camera roll followed by room classification. The checklist path passes the selected file directly; the separate AI chat path already has an image-compression helper.

Submission checks that the responsible person is selected and that each task is completed or has an explanatory note. Inventory uses an exceptions-only convention. I found no minimum-photo enforcement in the reviewed submit handler, despite Brandon recalling a minimum-photo requirement. That is a version/configuration/history question, not grounds to overwrite his account.

Approval for payout follows submission and creates a compensation ledger entry when configured. It does not prove that funds moved. The report that the cleaner stopped using completion features remains material evidence: code presence does not refute non-use.

Source anchors:

- [Checklist presentation](C:/Users/Brandon/Documents/Projects/airbnb/src/views/ChecklistView.vue:167), [photo upload](C:/Users/Brandon/Documents/Projects/airbnb/src/views/ChecklistView.vue:1490), [single-file control](C:/Users/Brandon/Documents/Projects/airbnb/src/components/checklist/ChecklistRowAttachments.vue:36).
- [Submission validation](C:/Users/Brandon/Documents/Projects/airbnb/app/Http/api.php:7717), [payout approval](C:/Users/Brandon/Documents/Projects/airbnb/app/Http/api.php:7375).
- [Automated checklist creation](C:/Users/Brandon/Documents/Projects/airbnb/app/Lib/cron_lib.php:484), [automation actions](C:/Users/Brandon/Documents/Projects/airbnb/app/Lib/cron_lib.php:2330).

## Existing AI and property knowledge can supply building blocks

The assistant accepts an image and text, supports speech dictation where the browser provides it, and calls backend tools subject to permissions. It can change records as well as read them. Uploaded inventory pictures and floorplan pins can be displayed in its replies. Those image URLs and pins do not themselves mean that every stored image is automatically supplied to the model for visual comparison.

For a readiness feature, reusable pieces include authentication, property/job context, file storage, image compression and server-side image input. New work would include job-level capture, approved room reference views, uncertain room labels, comparison results tied to evidence, missed-view handling and a simple cleaner response. Existing general-purpose chat should not silently become an automatic payout decision maker.

- [Assistant image and speech UI](C:/Users/Brandon/Documents/Projects/airbnb/src/components/admin/AdminAssistantTab.vue:100).
- [Image compression helper](C:/Users/Brandon/Documents/Projects/airbnb/src/lib/assistantImageAttach.ts:1).
- [Assistant tools and permissions context](C:/Users/Brandon/Documents/Projects/airbnb/app/Lib/assistant_chat_lib.php:1719).
- [Property wiki and inventory tools](C:/Users/Brandon/Documents/Projects/airbnb/app/Lib/assistant_chat_lib.php:53).

## Camera AI and LiDAR answer different parts of the problem

**Ordinary images:** proposed comparisons could flag a chair away from its reference position, an unset coffee station or an obviously missing item visible in the image. They need appropriate reference views, sufficient detail and evaluation against known examples. An unseen surface is unknown, and a missed detection must not appear as proof that the room is perfect. Fine dust, cleanliness behind objects, freshness, smells and whether linen was actually replaced are not established by a room photograph.

There is a close commercial comparison: [Properly's inspection product](https://getproperly.com/vacation-rental-inspection-software) advertises AI identification of staging/quality issues followed by human inspector confirmation. This is a vendor-described workflow, not independent evidence of its accuracy, or proof that an unattended two-programmer version will perform equally well.

**LiDAR/RoomPlan:** [Apple's RoomPlan overview](https://developer.apple.com/augmented-reality/roomplan/) describes a Swift API using camera and LiDAR for room dimensions and recognized furniture. That could contribute geometric evidence about larger furniture. It is not a cleanliness sensor or a ready-made detector for Mom's preferred coffee/spoon arrangement. The current web application would need a native Apple capture component/bridge to use RoomPlan.

**Device compatibility:** do not assume cleaners' phones have LiDAR. Apple's [iPhone 17 Pro specs](https://www.apple.com/iphone-17-pro/specs/) list it; the [standard iPhone 17](https://www.apple.com/iphone-17/specs/) does not. The current [iPad Pro](https://www.apple.com/ipad-pro/specs/) lists LiDAR; [iPad Air](https://www.apple.com/ipad-air/specs/) does not. These establish model differences, not a measured percentage of phones in this market. Exact compatibility should be checked before acquiring a device.

**Property-owned tablet:** a device the cleaner picks up for a final walkthrough could offer a consistent camera, screen, setup and charging location. Its usability benefit is separate from LiDAR. Carrying a tablet may be less comfortable than a phone, and charging/sign-in still need a simple arrangement. This is a handheld staff workflow, not a proposal for installed indoor monitoring. An ordinary camera device is sufficient to investigate image-based assistance first.

## A concrete proposed variant

1. Open today's job and tap **Final walkthrough**.
2. Take pictures in any order, with the camera kept readily available. No room selection before each shot.
3. The app suggests room grouping and a few visible setup corrections against Mom-approved references. Ambiguous room labels remain unresolved; unclear views say **Couldn't check**. Optional speech can explain an exception.
4. Send once and see a clear receipt. Mom sees the evidence, suggestions and unresolved checks; absence of a flag does not mean certified readiness.

Start by exploring ordinary photos; retain a short video pass as a separate capture variant. A video can reduce shutter taps but still adds walking, framing, upload and review work. Neither is validated yet.

The next useful input is whether Mom already has photos of rooms set up exactly as she wants them. If so, the facilitator can prepare a one-room reference/current comparison after suitable images are available. If not, identifying one room's reference setup comes first. A later probe should include correct scenes, actual or staged deviations, and unclear views, and record both missed issues and false alarms. No cleaner trial, worksheet or hardware purchase is assigned by this report.

## Finance issue found during inspection

The main totals classify `staff_compensation` as outflow, but the per-property summary's SQL omits that type from its outflow list and therefore counts it as inflow. Executing that exact per-property SELECT in an isolated SQLite database with one synthetic, confirmed $150 staff-compensation row returned **$150 inflow and $0 outflow**. The main helper classifies the same type as an expense. This fixture checks the aggregation expression, not the deployed MySQL service or real balances.

See [outflow classification](C:/Users/Brandon/Documents/Projects/airbnb/app/Http/api.php:2587) and [property summary query](C:/Users/Brandon/Documents/Projects/airbnb/app/Http/api.php:3230). No fix was made in this read-only review. Reconcile this inconsistency and input completeness before using the dashboard to judge profitability. The current labels also do not establish a complete accounting definition of profit or a reconciled bank balance.

## Mentor-room status

This advances Knapp–Zeratsky's current-alternative understanding and Pincus's separation of the need from implementation variants. H24 is now founder-preferred, not validated. H25 (assistive staging review) and H26 (a shared device) remain hypotheses. Foundation/core work, independent demand, willingness to pay, time savings and sustainable support costs remain incomplete. X03/X04 have not run.
