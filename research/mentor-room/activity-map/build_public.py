"""Build the resource coverage ledger from the user's unchanged CSV.

Access findings are research judgments, never inferred from a successful HTTP status.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROWS = list(csv.DictReader((ROOT.parent / 'resources.csv').open(encoding='utf-8-sig')))

# Every row is intentionally accounted for. Book coverage does not acquire interviews.
FINDINGS = {
1: ('summary_only', 'Podcast page and chapter markers available; speaker transcript absent from retrieved page. Full method covered separately by supplied Click and board.', ['click-book', 'character-board']),
2: ('supplied_asset', '114-page exported Character board is locally available and being reviewed page by page.', ['character-board']),
3: ('abridged_primary', 'YC publishes an explicitly shortened combined transcript. Hale segment is available; do not call it the complete original lecture.', ['yc-recap-1']),
4: ('unavailable', 'Video fetch failed; identity and the inventory claim that this is Part 2 remain unverified. No procedure inferred.', []),
5: ('primary_text', 'Creator transcript supplies the six-part 5PM screen and worked examples.', ['walling-628']),
6: ('primary_text', 'Creator transcript supplies context-dependent pricing/market clarification and further founder questions. No universal calibrated scoring system.', ['walling-840']),
7: ('summary_only', 'Publisher takeaways are available; full speaker dialogue is not rendered. Any proposed activity from these notes must be explicitly limited to the notes.', []),
8: ('summary_only', 'Publisher takeaways and chapter markers available; complete podcast dialogue not retrieved.', []),
9: ('summary_only', 'Podcast page available; supplied Pattern Breakers book is separately held and reviewed. These are different source objects.', ['pattern-book']),
10: ('primary_text', 'The GSB landing page has no talk transcript. Linked NFX article supplies five frameworks; it does not supply the advertised private additional frameworks.', ['nfx-patterns']),
11: ('primary_text', 'Ten opportunity lenses and a short iteration outline available. Actual author is Gigi Levy-Weiss, not James Currier as the CSV suggests.', ['nfx-pmf-places']),
12: ('primary_text', 'Twelve numbered advice sections accessible, with firsthand contributor statements. Linked underlying interviews are separate coverage.', ['fr-idea-frameworks']),
13: ('summary_only', 'Podcast notes available with paid written takeaways gate; no dialogue acquired. Pincus book separately supplies detailed methods.', ['pincus-book']),
14: ('summary_only', 'Podcast page accessible; full dialogue/book not acquired.', []),
15: ('summary_only', 'Podcast page accessible; full dialogue not acquired.', []),
16: ('supplied_book', 'The Right It is supplied in full; public methodology page separately checked. Linked talks are not automatically covered.', ['right-it-book']),
17: ('primary_text', 'Creator transcript provides staged effort in approximate hours, plus prior-art and design-decision advice.', ['walling-706']),
18: ('summary_only', 'Webinar page accessible; no substantive webinar transcript retrieved. Supplied TBI book is a separate source.', ['tbi-book']),
19: ('supplied_book', 'Complete supplied 365-page PDF, including all 44 experiments, is available for inventory.', ['tbi-book']),
20: ('offering_only', 'Training agenda/marketing is available; actual lesson materials and participant exercises are not acquired.', []),
21: ('bounded_primary', 'Official teachers page lists four activity types and chapter references. Full Mom Test book and examples are not supplied.', ['mom-teachers']),
22: ('abridged_primary', 'YC combined recap has an explicitly abridged Migicovsky interview lesson; original video transcript not retrieved.', ['yc-recap-1']),
23: ('primary_text', 'Full three-phase article accessible: plan, interview, analyze, including substeps and debrief variants.', ['mellinger-discovery']),
24: ('primary_text', 'Seven tactic sections accessible as selected founder accounts, not one prescribed serial program.', ['fr-validation-tactics']),
25: ('primary_text', 'Gagan Biyani first-person MVT article accessible, including procedure, cases and limits.', ['biyani-mvt']),
26: ('bounded_primary', 'Stanford course requirements and deliverables available; all lectures, readings and assignments are not acquired.', ['stanford-llp']),
27: ('bounded_primary', 'Author fill-order article available; full Running Lean book is not supplied. Article explicitly rejects a universal canvas fill order.', ['maurya-fill-order']),
28: ('offering_only', 'LEANSpark redirects to leanspark.ai. Marketing inspected; application not exercised and proprietary coaching workflow not acquired.', []),
29: ('bounded_primary', 'MIT link redirects to an HBR interview with Aulet. Official framework/worksheets are separate leads; full DE book is not supplied.', ['aulet-interview']),
30: ('offering_only', 'MIT Orbit public resource/access page inspected. Application not exercised; access-dependent JetPack outputs not acquired.', []),
31: ('bounded_primary', 'Torres public OST and assumption-testing guides available. Continuous Discovery Habits book/courses not supplied.', ['torres-ost', 'torres-assumptions']),
32: ('primary_text', 'Full SVPG four-risk article available; taxonomy and responsibilities, no numeric scorecard.', ['cagan-risks']),
33: ('primary_text', 'SVPG concept article and FAQ accessible. A distinction and decision frame, not a full workshop.', ['cagan-build']),
34: ('summary_only', 'Podcast page accessible; full JTBD speaker dialogue not retrieved.', []),
35: ('bounded_primary', 'Original interview page only partial. April Dunford official quickstart is a public first-person substitute; full book/interview not acquired.', ['dunford-positioning']),
36: ('summary_only', 'Podcast page accessible; full sales-pitch dialogue/book not acquired.', []),
37: ('summary_only', 'Twelve publisher takeaways accessible; no full speaker dialogue. They support a limited topic/tactic outline only.', []),
38: ('summary_only', 'Six publisher takeaways accessible; no full speaker dialogue. Growth anecdotes are not general validation evidence.', []),
39: ('summary_only', 'Podcast notes and chapter markers accessible; written takeaways gated, full dialogue not acquired.', []),
40: ('summary_only', 'Podcast page accessible; complete dialogue not acquired.', []),
41: ('summary_only', 'Podcast page accessible; complete founder-led sales dialogue not acquired.', []),
42: ('abridged_primary', 'Video page gives metadata only. Official YC Week 2 recap supplies shortened Seibel teaching, distinct from the full lecture.', ['yc-recap-2']),
43: ('offering_only', 'Course landing page/syllabus available; paid lessons, worksheets and guest interviews not acquired.', []),
44: ('summary_only', 'Podcast page and publisher framework summary available; complete dialogue not acquired.', []),
45: ('summary_only', 'Podcast page available; Vohra first-person article separately supplies PMF procedure.', ['vohra-pmf']),
46: ('primary_text', 'Full Vohra first-person PMF-engine account available. Survey/segmentation is for actual users, not fictional profiles.', ['vohra-pmf']),
47: ('primary_text', 'Public overview available with survey and metrics recommendations. This overlaps #46 but is not the same source.', ['fr-measure-pmf']),
48: ('primary_text', 'Twenty numbered founder lessons available. Treat case tactics as conditional alternatives rather than twenty required stages.', ['fr-pmf-paths']),
49: ('collection', 'Navigation collection retrieved. Membership is a changing list of separate resources, not an exercise or closed curriculum; listed CSV items are tracked individually.', []),
}

def build():
    result = []
    for row in ROWS:
        number = int(row['Recommended_Order'])
        status, finding, related = FINDINGS[number]
        result.append({
            'id': f'R{number:02}', 'inventory_row': number,
            'title': row['Resource_Title'], 'author_from_inventory': row['Person_or_Author'],
            'kind_from_inventory': row['Resource_Type'],
            'url': row['Primary_Link'], 'secondary_url': row['Secondary_Link'],
            'access_status': status, 'finding': finding,
            'related_source_ids': related, 'reviewed_on': '2026-09-09',
            'candidate_topics_from_inventory': row['Key_Frameworks_or_Topics'],
            'candidate_output_from_inventory': row['Practical_Output'],
            'metadata_warning': 'Candidate topics/outputs are supplied metadata, not acquired procedures.',
        })
    assert {r['inventory_row'] for r in result} == set(range(1, 50))
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'data/public-access.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Wrote {len(result)} coverage records')

if __name__ == '__main__':
    build()
