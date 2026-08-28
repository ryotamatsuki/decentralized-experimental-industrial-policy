# Stage 5 — C4 Mechanism Hardening

## 1. Executive verdict

- **Canonical verdict:** `NO-GO`
- **Research decision:** `C4 TERMINATED AT STAGE 5`
- **Stage 4 blocker resolved mathematically?** `YES`
- **Did the one modification create a defensibly distinct mechanism?** `NO`
- **Stage 6:** `NOT AUTHORIZED / NOT EXECUTED`

The only authorized modification, host-dependent information productivity `q_i`, successfully makes the information produced by the trial enter the hosting competition itself. A low-information jurisdiction bids less aggressively for a trial when losing to a high-information host produces better evidence for it.

However, the resulting strategic structure is not sufficiently novel. The active hosting game is a special case of an allocation/auction with **identity-dependent externalities**: a losing government's payoff depends on which jurisdiction wins. The high-reserve block becomes an asymmetric volunteer/public-good problem, while the planner's site-quality criterion is closely related to heterogeneous experimentation and external-validity site selection.

The Stage 4 blocker is therefore repaired, but the repair reveals that C4 is structurally inside known theory families. A second substantive modification would be required to escape them, and Stage 5 governance expressly forbids a second rescue.

## 2. Exact Stage 4 blocker

> **The informational value of the launch trial is invariant to host location and therefore does not feed back into the hosting competition; as a result, the current C4 baseline partially collapses to ordinary mobile-project subsidy bidding plus a separate free-riding wedge.**

## 3. One authorized modification

Introduce only

`q_i>0`:

> the generalizable information/learning quality produced by the launch trial when jurisdiction `i` hosts.

If jurisdiction `i` hosts, both jurisdictions receive information/adoption benefit `q_i E`.

No `H_i`, `C_i`, `V_i`, private information, supplier effort, disclosure, dynamics, second knowledge stock, multiple suppliers or other rescue mechanism was added.

## 4. Economic microfoundation of q_i

`q_i` captures whether the local implementation field makes the same technology trial more or less informative for later adoption elsewhere—e.g. differences in implementation environment, observable user mix, production setting or external validity.

It is deliberately not a generic profitability shifter:

- supplier continuation value `V` remains host invariant;
- host-only local benefit `H` remains common;
- when `E -> 0`, all `q_i` effects disappear from the hosting bids.

Thus the primitive is economically coherent and experiment-specific.

## 5. Revised model

Two jurisdictions `i=1,2`, one supplier, one launch trial.

Frozen primitives:

- `C>0`: trial resource cost;
- `V>=0`: supplier downstream commercialization value;
- `F=C-V`: supplier financing gap;
- `E>0`: baseline value of trial evidence;
- `H>0`: host-only local benefit;
- `mu>0`; `k=1+mu`.

New primitive only:

- `q_i>0`: information productivity of a trial hosted in i.

If `i` hosts at subsidy `s_i`:

- supplier payoff: `s_i-F`;
- host government payoff: `q_i E + H-k s_i`;
- nonhost government payoff: `q_i E`.

If no trial occurs, payoffs are zero.

Aggregate welfare at host i is

`W_i(s_i)=2q_iE+H-F-mu s_i`.

## 6. Full equilibrium: key affected blocks

Take `q_1>q_2` without loss of generality and define `Delta_q=q_1-q_2>0`.

Local unilateral-financing values:

`Ubar_1=(q_1E+H)/k`,

`Ubar_2=(q_2E+H)/k`.

Maximum subsidy to take hosting away from the rival:

`D_1=[H+E Delta_q]/k`,

`D_2=[H-E Delta_q]/k`.

Exact identities:

`D_1-D_2=2E Delta_q/k`,

`D_1+D_2=2H/k`.

The high-information site is more willing to take hosting from the low-information site; the low-information site is less willing to take hosting from the high-information site.

In the low-reserve active-contest block, complete-information continuous first-price bidding has the standard asymmetric discontinuity. A vanishing monetary bid grid is used only as a technical regularization. In the limit, the high-q site hosts and its subsidy is

`s_1^D=max{max(F,0),D_2,0}`

when the trial is locally supportable.

For `F>0`, the high-q pure volunteer equilibrium `(F,0)` exists when `F>=D_2` and `F<Ubar_1`.

A low-q volunteer equilibrium `(0,F)` exists iff

`D_1<F<Ubar_2`.

That interval is nonempty iff

`q_1<2q_2`.

Hence q heterogeneity does not generate a unique low-q allocation. It generates multiplicity/coordination in a region where both jurisdictions can volunteer.

## 7. Participation / existence / corners

Supplier participation remains frozen:

- if `F<=0`, trial is privately viable without public support;
- if `F>0`, the winning subsidy must be at least `F`.

If `F>Ubar_1`, neither jurisdiction covers the gap and there is no decentralized trial.

If `E Delta_q>=H`, then `D_2<=0`: the low-q jurisdiction has no positive willingness to pay merely to take a privately viable trial away from the high-q jurisdiction.

Boundary equalities create weak/multiple outcomes and are excluded from strict propositions.

## 8. Local hosting willingness — Stage 4 blocker resolution

This is the main successful hardening result.

Stage 4 had host-contest value

`H/k`.

Stage 5 gives the low-quality region's contest value

`D_2=H/k-E Delta_q/k`.

Therefore

`partial D_2 / partial Delta_q=-E/k<0`.

The reason is strategic and experiment-specific: if jurisdiction 2 loses to the high-q jurisdiction 1, jurisdiction 2 itself receives better information `q_1E`. Its outside option from losing improves, so it pays less to steal hosting.

Thus experimental information now feeds back directly into host bidding.

## 9. Social benchmark

At equal real trial cost and supplier value, the planner selects host 1 because `q_1>q_2`.

For `F>0`, minimum support is `F` and the high-quality social trial threshold is

`S_1=(2q_1E+H)/k`.

The planner induces the high-q trial iff `F<S_1`.

At the same subsidy, the real welfare loss from choosing host 2 is

`W_1-W_2=2E Delta_q>0`.

## 10. Decentralized versus social host choice

### Active-contest region

The high-q jurisdiction wins in the vanishing-grid limit. Therefore the model does **not** generate systematic low-q mislocation in the central hosting-auction block.

### Volunteer region

A socially inferior low-q pure volunteer equilibrium coexists with the high-q equilibrium when

`D_1<F<Ubar_2`,

which requires `q_1<2q_2`.

In the completely mixed volunteer equilibrium, define

`A_i=q_iE+H-kF`.

Funding probabilities are

`p_1=2A_2/(A_2+q_1E)`,

`p_2=2A_1/(A_1+q_2E)`.

Exact difference:

`p_2-p_1 = 2E(q_1-q_2)/[E(q_1+q_2)+H-kF] >0`.

Thus the lower-q jurisdiction funds—and therefore hosts—more often in the completely mixed equilibrium. This is a valid result, but it is a coordination/asymmetric-volunteer result rather than a unique experiment-location prediction.

## 11. Subsidy comparison

### Private launch `F<=0`

Stage 4 always had positive host bid `H/k`.

Stage 5 limiting subsidy is

`max{D_2,0}`.

Hence information quality can discipline a wasteful hosting race:

- `H>E Delta_q`: a reduced positive host subsidy remains;
- `H<=E Delta_q`: the low-q rival will not pay to steal the trial, so the host-race subsidy falls to zero in the limit.

### Support needed

For `0<F<Ubar_1`, high-q equilibrium support is

`max{F,D_2}`.

If `F<D_2`, decentralized bidding overpays by `D_2-F`, generating supplier rent and fiscal loss `mu(D_2-F)` relative to minimum-gap support.

If `F>=D_2`, the high-q equilibrium pays only the financing gap.

## 12. Revised regime map

For `q_1>q_2`:

1. **private launch / no contest**: `F<=0` and `D_2<=0`;
2. **private launch / information-disciplined host contest**: `F<=0<D_2`;
3. **support-needed overpayment**: `0<F<D_2`;
4. **high-quality minimum support**: `max{D_2,0}<=F<Ubar_1`;
5. **under-experimentation**: `Ubar_1<F<S_1`;
6. **efficient no trial**: `F>=S_1`.

Inside the minimum-support range, a low-q volunteer equilibrium can additionally coexist when `D_1<F<Ubar_2`.

## 13. What changed relative to Stage 4

Changed substantively:

- the rival-host identity changes the losing jurisdiction's information payoff;
- host bids directly depend on information quality;
- better experimental quality can reduce or eliminate host-race subsidy;
- host-quality multiplicity/coordination becomes possible.

Did not change:

- supplier downstream value remains an exogenous participation term;
- generic fiscal rent competition survives;
- the local/social experiment-financing wedge remains standard partial internalization;
- a unique socially wrong host does not arise from q_i alone.

## 14. Candidate-proposition kill table

| Candidate | Mathematical status | Stage 5 research status |
|---|---|---|
| P5.1 information-sensitive hosting bid | `PROVED` | `KILLED AS MAIN NOVELTY` — special case of identity-dependent externality auction |
| P5.2 local vs social information valuation | `PROVED` | `KILLED AS MAIN NOVELTY` — standard partial internalization |
| P5.3 mislocation | `ONLY MULTIPLICITY / MIXED PROBABILITY` | `KILLED AS HEADLINE` — no unique mislocation; close volunteer-dilemma logic |
| P5.4 wasteful competition with q | `PROVED, QUALIFIED` | `BACKGROUND/SECONDARY` — local subsidy competition prior art remains close |
| P5.5 governance implication | `BENCHMARK DERIVABLE` | `NOT SUFFICIENT FOR NOVELTY` |

## 15. Reduction tests

- `q_1=q_2=1`: exact Stage 4 threshold recovery — PASS.
- `E->0`: q effects disappear from bids — PASS.
- `H->0`: host-rent contest disappears — PASS.
- `V->0`: private-launch zero-additionality region disappears — PASS.
- `mu->0`: fiscal transfer loss disappears while real low-q information loss remains — PASS.
- `q_1/q_2->1`: Stage 4 structure is approached continuously — PASS.

## 16. Symbolic verification

`code/stage5_c4_q_verify.py` verifies all material identities with SymPy, including:

- contest-value differences;
- local/social thresholds;
- Stage 4 nesting;
- mixed-strategy funding probabilities;
- host-probability difference;
- welfare gaps.

No reported closed form relies on numerical approximation.

## 17. Numerical counterexample audit

Seed: `20260828`.

300,000 / 300,000 raw/feasible draws.

Main counts:

- private launch, q gap eliminates contest: 62,074;
- private launch, positive contest: 112,083;
- support-needed contested overpayment: 16,164;
- high-q minimum support: 54,158;
- under-experimentation: 20,336;
- efficient no trial: 35,185.

Low-q pure-volunteer/mislocation equilibrium existed in 11,364 draws, overlapping the minimum-support category.

Violations:

- analytical region/sign conditions: 0;
- mixed-equilibrium probability/indifference conditions: 0;
- mislocation interval condition: 0.

Numerics confirm positive-measure regions but are not proofs.

## 18. Prior-art re-check

The hardening reveals a stronger prior-art problem than Stage 4.

### Jehiel, Moldovanu & Stacchetti (1999)

Their auctions-with-externalities framework explicitly allows a losing bidder's payoff to depend on the identity of the winner. That is exactly the Stage 5 strategic innovation generated by `q_i`.

### Jehiel & Moldovanu (2000)

Auction outcomes affect buyers' downstream payoffs; reserve/retention and welfare effects are analyzed.

### Slattery (2025) / Mast (2020)

The fiscal-rent and low-additionality side remains standard local subsidy competition.

### Callander & Harstad (2015)

Heterogeneous experimentation plus informational spillovers and decentralized distortion are already established.

### Gechter et al. (2024–2026 circulation)

Choosing experimental sites for external validity already establishes that site choice can change generalizable evidence and welfare.

### Volunteer-dilemma literature

Multiple pure equilibria and inefficient/counterintuitive volunteers are already known; the low-q volunteer block cannot carry novelty.

The exact institutional combination was not found, but the strategic blocks are structurally known. Search failure is not novelty evidence.

## 19. Skeptical referee attack

The strongest attack succeeds:

> once q_i is introduced, the new feedback is precisely that a losing jurisdiction cares who wins because the winner determines the common information outcome.

That is an identity-dependent allocation externality. The model therefore became mathematically more integrated but also more directly mapped to a mature auction-theory class.

The one permitted change does not clear the novelty gate.

## 20. Artefact / mechanical-result audit

`q_i` is **not** decorative and does **not** mechanically impose unique mislocation. This is a positive modeling result.

But the surviving results fail for a different reason: the strategic mechanism they create is structurally known.

Attempting to obtain a unique, distinct experiment-location distortion would require another primitive or strategic margin—e.g. host-dependent supplier value, effort, private information, differentiated local rent, disclosure, dynamics, etc. Every such route is a prohibited second Stage 5 repair.

## 21. Remaining blocker

There is no admissible narrow blocker suitable for another `CONDITIONAL GO`.

The problem is now **contribution-level**:

> the only authorized hardening maps C4 into known identity-dependent externality-auction / asymmetric-volunteer structures, and escaping them requires a second substantive mechanism.

Under canonical governance this is a branch-kill condition, not a reason for further hardening.

## 22. Canonical verdict

**`NO-GO`**

C4 is terminated at Stage 5.

The Stage 4/5 mathematical results remain valid as documented negative/background findings, but C4 should not be presented as the main new theory contribution.

## 23. Next-stage contract

- **Do not execute Stage 6 for C4.**
- **Do not add a second repair to C4.**
- **Do not automatically pivot to C6 or C3.**
- If research continues, the Human Research Director must return to the Stage 3 candidate set and explicitly choose a genuinely distinct mechanism for a new branch.

**STOPPED AFTER STAGE 5 — NO STAGE 6 EXECUTION.**
