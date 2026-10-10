# Stage 11D — Chief Architect Final Adjudication

**Adjudication: FINAL / SCORING COMPLETE**  
**STAGE11_HOLDOUT_GATE: FAIL**  
**Agent v0.2: EVALUATED / FORMAL RELEASE NOT APPROVED**

## 1. Immutable evaluation references

- Paired evidence SHA: `113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a`.
- Independent scorer SHA: `7770564acc2db7d244d933db5ff089a33c9197fc`.
- Holdout design SHA: `69cab5ab750c350ce719a0d37e7680bbc96bdf21`.
- Rubric SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`.
- v0.1 SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`.
- v0.2 SUT: `c12b67c7410878960c45a9934ded6ae52ae6c42f`.
- Shared company gateway model: `glm-5.3`.
- Both measured runs: 12/12 COMPLETE, same 12 input payloads, 24 nonempty final outputs, 29 canonical files, zero technical retries/failures.
- This adjudication makes no model calls, changes no frozen SUT/raw/oracle/rubric, and does not change a preregistered gate.

## 2. Decision

The Chief Architect reviewed all seven case IDs flagged for adjudication, including both versions where relevant: H11-001, H11-002, H11-004, H11-005, H11-007, H11-009 and H11-011.

Stratified spot checks: H11-006, H11-010 and H11-012 across both versions.

**No score, hard-failure registration or applicable-dimension adjustment is justified.** The scorer's published scores and seven-gate verdict are accepted as final.

| Measure | v0.1 | v0.2 | Change |
|---|---:|---:|---:|
| Overall | 184/212 (86.79%) | 176/212 (83.02%) | −8 points; −3.77 percentage points |
| D3 evidence discipline | 16/24 (66.67%) | 15/24 (62.50%) | −1 point; −4.17 pp |
| HF-03 distinct case registrations | 4 | 4 | 0% reduction |
| Accepted primary route | 12/12 | 12/12 | no regression |
| Strict GOOD CASE material false positives | 0 | 0 | no regression |
| Global terminal correct | 12/12 | 12/12 | no regression |

Gate results: **C1 FAIL, C2 FAIL, C3 PASS, C4 PASS, C5 PASS, C6 FAIL, C7 PASS.** All seven criteria are conjunctive; the holdout gate FAILS.

## 3. Hard-failure adjudication

### H11-001, v0.1 — HF-03 upheld

The provided pilot sample was hand-selected, but its selection distribution was not recorded. Saying hand selection *systematically avoids pathological sizes* asserts an unprovided selection direction. Its general non-representativeness is a sound observation; the direction-specific project fact is not.

Ruling: v0.1 HF-03/D3=0 stands. The v0.2 answer does not repeat this unsupported assertion, so its improved D3=2 stands.

### H11-002, both — HF-01 upheld; HF-03 upheld

Both versions elevate the limited camera export's capture-provenance gap to a supported material BLOCKER. The provided export lacks the relevant fields, but retained on-camera image metadata or external logs are explicitly unresolved. The finding's claimed non-capture/non-derivability exceeds the evidence for a full six-pillar blocker under the frozen rubric and oracle.

v0.2 additionally states that firmware replacement *destroyed* pre-replacement controller history and therefore the historical evidence is *not collectible*. The case only says firmware was replaced before export and does not state whether its history was destroyed or retained elsewhere. That is a load-bearing project-specific false assertion, used to exclude a discriminator.

Ruling: HF-01 for both stands; HF-03 for both stands. The additional v0.2 uncertainty penalty on D8 is justified. Main incident attribution staying NEEDS_EVIDENCE does not cure local false certainty.

### H11-004, both — HF-03 and HF-05 upheld

The supplied production output/histogram omit specific linkage fields, and no per-output revision mapping was supplied. Both versions go further and state globally that the attribution evidence was never captured / retained anywhere and cannot be derived. Other possible source ledgers are not ruled out. This is the frozen HF-03 distinction between "not supplied here" and "does not exist".

The accepted published metre convention is coupled to an exchange test that **expects the yard-valued fixture to be converted to metres**. Both answers propose refusing the already supported non-metre input as the complete correction rather than ensuring the conversion on all supported paths. Fail-closed refusal is a valid temporary containment, but not proof of the accepted full support/functional guarantee; presenting it as the complete fix silently drops that supported path. This satisfies the frozen HF-05 trigger, **applied symmetrically to both versions**.

Ruling: both HF-03 and HF-05 stand. This is a shared weakness, not v0.2-specific regression.

### H11-005, v0.2 — HF-03 upheld

Passing recovery tests for documented deployment procedures is not equivalent to demonstrating that the architecture **decision** between A/B can be reversed with acceptable migration/cost/compatibility characteristics. The v0.2 statement that both are reversible promotes limited test evidence into an established, broader project fact.

The answer also overstates governance risk where the frozen oracle permits preference/nonblocking dispositions. The overall OWNER_TRADE_OFF terminal is nevertheless correct.

Ruling: HF-03/D3=0 and the separate D9 deduction stand.

### H11-009 — v0.1 no HF, v0.2 HF-03 upheld

v0.1's UI-loop ownership description is a bounded mechanism-level synthesis of the CODE/CONFIG/TEST facts that all map mutations take place in one non-reentrant UI loop. It does not establish a fabricated concrete cleanup implementation. No HF is warranted there.

v0.2 states that the invariant is *currently enforced only by tests and the runtime contract*. The provided facts establish those forms of enforcement but do not exclude other existing checks. The word **only** is an unsupported exclusion of other project mechanisms, used to motivate an improvement. The global NO_DEFECT remains correct; however, the local NEEDS_EVIDENCE finding on an already refuted race is an output-contract defect.

Ruling: v0.1 no-HF stands; v0.2 HF-03/D3=0 and D9=1 stand; no material GOOD CASE false positive was triggered.

### H11-011 — v0.1 HF-03 upheld; v0.2 no HF

The packet describes a prepared rollout and registered reader/writer combinations, not the entire code diff. v0.1's absolute assertion that **no diff hunk exists outside the signer-epoch variation axis** is therefore an unsupported project fact. v0.2 grounds its conclusion in the supplied staged behavior and avoids that absolute negative.

Both choose the same justified primary CHANGE_REVIEW/DP-003 and NO_DEFECT. v0.2 omits an expected evolution overlay, which legitimately affects D1 without changing primary-route acceptance.

Ruling: v0.1 HF-03/D3=0 stands; v0.2 no HF and partial D1 stand.

## 4. Non-HF disputed boundary

### H11-007, v0.2 — correction undercoverage upheld, but no HF-05 added

v0.2 correctly identifies that issuance authorization does not protect already-issued signed URLs, but its proposed API/front-end mediation describes **future** downloads without closing the existing direct-to-storage URL path. Previously issued links remain valid at the original endpoint under given CONFIG. It does not show a complete mechanism by which post-removal reads through that path are refused.

That is a real minimum-correction/guarantee-sufficiency defect, justifying D6=1, D7=1, D9=1. The answer does not positively authorize a grace period or state that existing links may continue to work after removal; do not escalate the omission into HF-05 without the frozen trigger.

## 5. Stratified spot checks

- **H11-006:** Both versions acknowledge that the tested board-identity check has limited real value while interrupted-boot qualification remains unresolved. v0.2's hypothetical other-flashing-channel check is an out-of-scope carry-over, not an invented currently existing channel. D10 minor deduction is proportionate; no HF.
- **H11-010:** Both versions protect the compliant immutable-manifest/content-addressed-cache arrangement. No material GOOD CASE false positive or hidden requirement appears. Scores remain equal.
- **H11-012:** Both versions detect the publication-before-review defect, distinguish job ownership from publication ordering, and require all included components to finish review before bytes are exposed. v0.2's join plus reviewed-output-only assembly is mechanism-equivalent to the oracle's sufficient local correction; no specific snapshot/hash implementation name is mandatory. D6=2 for both. A small v0.2 scope advantage explains its one-point improvement.

These checks found no score adjustment or latent material hard-failure registration.

## 6. Outcome interpretation and next action

**The measured v0.2 revision did not improve evidence discipline in this holdout.** It removed HF-03 cases H11-001 and H11-011 but introduced H11-005 and H11-009; H11-002/H11-004 remain shared. It preserved route and strict GOOD CASE performance while regressing in evidence discipline, correction sufficiency and local finding/terminal alignment.

This result is specific to the exact 12 frozen cases, one canonical run per candidate, the company `glm-5.3` model, and the frozen Harness. No statistical significance or cross-model superiority is claimed. Yet the preregistered release gate unambiguously fails, and the score is not to be rescued by post-hoc threshold changes or re-running favorable samples.

Final states:

- `STAGE11_C: PASS / TECHNICALLY COMPLETE`
- `STAGE11_D: COMPLETE / ADJUDICATED`
- `STAGE11_HOLDOUT_GATE: FAIL`
- `AGENT_V0.2: EVALUATED / FORMAL RELEASE NOT APPROVED`

**Product recommendation:** prioritize making the previously evaluated v0.1 contract accessible as a clearly labeled, human-reviewed Codex Beta. v0.2 may remain an explicitly experimental option, not the unqualified default. Neither version should make unattended, binding high-impact architecture/product decisions. Do not launch another large evaluation-infrastructure project.

No Agent, KB, Harness, scorer, oracle, PUBLIC case, run evidence or frozen pass criteria changed by this report.
