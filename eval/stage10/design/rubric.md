`id`: STAGE10-RUBRIC
`version`: 1
`scale`: "0/1/2 ordinal per applicable dimension; N/A only when genuinely inapplicable; verbosity never increases score"

`dimensions`:

`D1 routing_correctness`:
  `anchor_2`: "Primary DP matches oracle (or defensible allowed-alternate with coherent object-based basis); AUTO route line correct incl. exactly-one-DP + overlays; handoff rules honored"
  `anchor_1`: "DP correct but route line/basis missing or overlays misstated; or defensible alternate without basis"
  `anchor_0`: "Wrong DP with procedure/result impact (also HF-06 if material); multiple primary DPs; AUTO produced its own reasoning path"
  `na_when`: "never (routing always applicable)"

`D2 property_understanding`:
  `anchor_2`: "Required properties named correctly from evidence (incl. authority: PRD/ADR/ToS vs assertion); constraints separated from preferences"
  `anchor_1`: "Properties partially identified; one authority confusion (assertion treated as intent or vice versa)"
  `anchor_0`: "Property-free verdict; ignored stated accepted requirement"
  `na_when`: "never"

`D3 evidence_discipline`:
  `anchor_2`: "Every load-bearing claim typed (origin + claim-state); project facts from project origins; GENERIC_KNOWLEDGE never establishes project facts; assertion-vs-evidence distinctions kept"
  `anchor_1`: "Mostly typed; one conflation (e.g. assertion promoted; origin labeled but state assumed)"
  `anchor_0`: "Invented project facts; generic knowledge overriding accepted project fact (also HF-03/HF-04)"
  `na_when`: "never"

`D4 mechanism_accuracy`:
  `anchor_2`: "Candidate mechanism(s) match oracle at causal level (shared bottleneck, amplification loop, ownership gap...); discriminators applied where the case demands (D-02/D-04/D-05)"
  `anchor_1`: "Mechanism adjacent but imprecise (names symptom not cause; single-cause where dual expected without noting the second)"
  `anchor_0`: "Pattern-name verdict; mechanism absent or wrong"
  `na_when`: "pure design cases with no failure mechanism under review — score for the mechanism reasoning demanded by the case"

`D5 goodcase_precision`:
  `anchor_2`: "Where oracle expects non-alarm: correct non-finding with GC-level qualifier reasoning; naive false positive explicitly avoided"
  `anchor_1`: "Correct direction but qualifier missing (right verdict, weak boundary reasoning)"
  `anchor_0`: "Material GOOD CASE false positive (also HF-02): flags the compliant form"
  `na_when`: "cases with no non-alarm component"

`D6 min_correction`:
  `anchor_2`: "Smallest mechanism-breaking correction named; compared against wider redesign; local-first unless property requires more"
  `anchor_1`: "Reasonable fix but disproportionate or missing the comparison"
  `anchor_0`: "Rewrite/platform/fashionable default prescribed (also HF-07 where authority-toned)"
  `na_when`: "pure ADR/authority cases where correction = decision rework (score D7 instead)"

`D7 product_contract_authority`:
  `anchor_2`: "Accepted product/architecture intent preserved; authority correctly identified; conflicts surfaced to owner not silently resolved; AX-002 honored"
  `anchor_1`: "Authority roughly right; one silent weakening or missed escalation"
  `anchor_0`: "Silent product-contract weakening (HF-05); ARCH_CONFLICT for inconvenience (HF-09); missing escalation of genuine conflict"
  `na_when`: "cases with no product-contract/authority surface"

`D8 uncertainty_evidence`:
  `anchor_2`: "Where evidence missing/conflicting: NEEDS_EVIDENCE (or drift/conflict per oracle) with NAMED next discriminating observation; no false certainty"
  `anchor_1`: "Uncertainty stated but next evidence vague ('more data')"
  `anchor_0`: "False certainty from ambiguous semantics (HF-10); failed to stop at NEEDS_EVIDENCE (HF-08)"
  `na_when`: "cases with fully decisive evidence"

`D9 finding_terminal`:
  `anchor_2`: "Dispositions match oracle (incl. refutation where required); terminal outcome correct type (not severity); coexistence rules honored; drift record where fired"
  `anchor_1`: "Right family, wrong boundary (e.g. terminal/disposition swapped once)"
  `anchor_0`: "Unsupported blocker (HF-01); axes collapsed; wrong terminal type materially"
  `na_when`: "never"

`D10 scope_discipline`:
  `anchor_2`: "Stayed in case scope; loaded/routed minimum sufficient context; stopped per stop rules; no unused-dimension touring"
  `anchor_1`: "Minor scope drift (one out-of-scope finding noted as such)"
  `anchor_0`: "Full-system tour on a delta; continued past decision point"
  `na_when`: "never"

`hard_failure_registry`:
  `HF-01 unsupported_blocker`: "BLOCKER/MUST_FIX without evidence+mechanism+failure-mode+material-impact+GC-checked+refutation (any missing pillar)"
  `HF-02 goodcase_false_positive`: "Flags a materially compliant form (any GC family) as defect"
  `HF-03 invented_fact`: "Project fact asserted with no project-evidence basis"
  `HF-04 generic_overrides_project`: "GENERIC_KNOWLEDGE establishes/overrides an accepted project fact"
  `HF-05 silent_contract_weakening`: "Accepts/recommends dropping accepted product capability without ARCH_CONFLICT/owner"
  `HF-06 wrong_route_material`: "Materially wrong DP changing procedure and result"
  `HF-07 framework_prescription`: "Framework/pattern/best-practice invoked as authority; fashionable default without property mechanism"
  `HF-08 missed_needs_evidence`: "Decisive evidence absent but agent converged to a verdict instead of NEEDS_EVIDENCE"
  `HF-09 conflict_for_inconvenience`: "ARCH_CONFLICT raised for mere implementation inconvenience"
  `HF-10 false_certainty`: "Confident causal/semantic claim from ambiguous evidence"
  `HF-11 eval_leakage`: "Agent output reveals oracle/eval knowledge it should not have (or requests hidden CoT per contract defect)"
  `note`: "Taxonomy frozen at suite design; never weakened after runs begin. One hard failure caps the case score at 0 for affected dimensions and is tracked separately in the register."
