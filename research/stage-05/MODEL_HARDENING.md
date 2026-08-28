# Stage 5 — C4 Model Hardening

## 1. Previous failure

Stage 4 blocker, quoted verbatim:

> **The informational value of the launch trial is invariant to host location and therefore does not feed back into the hosting competition; as a result, the current C4 baseline partially collapses to ordinary mobile-project subsidy bidding plus a separate free-riding wedge.**

The only authorized repair is host-dependent information productivity.

## 2. One allowed modification

Introduce `q_i>0`, the generalizable information/learning quality produced when jurisdiction `i` hosts the launch trial.

If `i` hosts, **both** jurisdictions receive information/adoption value `q_i E`. This is intentionally the smallest interpretation that makes host identity change the common evidence produced by the experiment. No host-specific `C_i`, `V_i`, `H_i`, private information, effort, dynamics, disclosure, or second knowledge stock is added.

`q_i` is therefore not a generic location-profit shifter for the supplier: supplier commercialization value `V` remains host invariant.

## 3. Frozen primitives and timing

Two local governments `i=1,2`, one supplier and one launch trial.

- `C>0`: real trial cost.
- `V>=0`: supplier downstream commercialization value conditional on any trial.
- `F=C-V`: supplier financing gap.
- `E>0`: baseline per-jurisdiction value of generalizable trial evidence.
- `q_i>0`: host-specific productivity of that evidence.
- `H>0`: host-only early-use/place benefit.
- `mu>0`: marginal excess burden of public subsidy.
- `k=1+mu`.

Timing remains Stage 4:

1. governments simultaneously announce host-contingent subsidies `s_i>=0`;
2. supplier observes offers and selects no trial / host 1 / host 2;
3. a hosted trial produces downstream commercialization value and evidence.

Supplier payoff if `i` hosts:

`Pi_S(i)=s_i-F`.

Hence host quality does **not** directly enter supplier payoff.

## 4. Government payoffs

If `i` hosts:

`U_i^H(i)=q_i E + H - k s_i`.

If `j` hosts:

`U_i^N(j)=q_j E`.

If no trial occurs:

`U_i^0=0`.

The information quality of the losing outcome is now payoff relevant. This is precisely the Stage 4 block that changes.

## 5. WLOG ordering and local thresholds

For the asymmetric analysis let

`q_1>q_2>0`

and define

`Delta_q=q_1-q_2>0`.

### 5.1 Willingness to volunteer when otherwise no trial occurs

`Ubar_i=(q_i E+H)/k`.

Thus

`Ubar_1>Ubar_2`.

### 5.2 Willingness to take hosting away from the other jurisdiction

Relative to jurisdiction 2 hosting, jurisdiction 1's maximum subsidy is

`D_1=[H+E(q_1-q_2)]/k`.

Relative to jurisdiction 1 hosting, jurisdiction 2's maximum subsidy is

`D_2=[H-E(q_1-q_2)]/k`.

Therefore

`D_1-D_2=2E Delta_q/k`,

`D_1+D_2=2H/k`.

Crucially, the lower-information jurisdiction's willingness to contest the high-information host is reduced by the information it would lose by relocating the experiment:

`D_2=H/k-E Delta_q/k`.

This is the direct Stage 5 feedback from experimental information to host bidding.

Useful identities:

`Ubar_1-D_1=q_2 E/k>0`,

`Ubar_2-D_2=q_1 E/k>0`.

## 6. Social benchmark

If host `i` is selected with subsidy `s`, aggregate welfare is

`W_i(s)=2q_i E+H-F-mu s`.

For identical `C,V,H` across sites, the social planner strictly prefers host 1 whenever `q_1>q_2`.

For `F>0`, minimum inducing support is `F`, so the social trial threshold at the best site is

`S_1=(2q_1 E+H)/k`.

The planner induces a host-1 trial iff `F<S_1`.

For `F<=0`, the trial is privately viable and the planner uses zero subsidy and host 1.

The welfare loss from using host 2 instead of host 1 at the same subsidy is exactly

`W_1(s)-W_2(s)=2E Delta_q>0`.

## 7. Continuous-bid technical issue and epsilon-grid regularization

With `q_1!=q_2`, the low-gap simultaneous continuous first-price hosting game has the familiar complete-information discontinuity: the high-value bidder wants to outbid the low-value bidder by an arbitrarily small amount, so a strict pure equilibrium generally does not exist under symmetric tie breaking.

This is a **technical**, not substantive, issue created by the Stage 5 asymmetry. We therefore use a vanishing monetary bid grid `epsilon>0` only to characterize the limiting equilibrium outcome. No economic proposition depends on a positive `epsilon`.

As `epsilon -> 0`, when both jurisdictions actively contest a trial, jurisdiction 1 wins and the winning subsidy converges to the lower-quality jurisdiction's contest value, truncated at zero and at the supplier participation reserve.

Define the participation reserve

`r=max{F,0}`.

The high-quality-host limiting subsidy is

`s_1^D=max{r,D_2,0}`

whenever the trial is locally supportable (`F<Ubar_1` when `F>0`).

## 8. Equilibrium blocks for q_1>q_2

### 8.1 Low reserve / active hosting competition

If

`r < D_2`

(with necessarily `D_2>0`), both jurisdictions contest hosting. In the vanishing-grid limit:

- host: jurisdiction 1;
- subsidy: `s_1 -> D_2`;
- supplier excess rent over the reserve: `D_2-r`.

The information-quality gap directly lowers the winning subsidy:

`partial D_2 / partial Delta_q = -E/k <0`.

If `E Delta_q >= H`, then `D_2<=0`: the lower-quality jurisdiction does not value taking the trial away from the high-quality host, and the host-rent bidding component collapses.

### 8.2 High-quality minimum-support equilibrium

For `F>0`, if

`F>=D_2` and `F<Ubar_1`,

`(s_1,s_2)=(F,0)` is a pure equilibrium (up to inactive offers below `F`). Jurisdiction 1 finances exactly the supplier gap; jurisdiction 2 does not profitably outbid it.

### 8.3 Low-quality volunteer / mislocation equilibrium

`(s_1,s_2)=(0,F)` is also a pure equilibrium iff

`D_1<F<Ubar_2`.

This interval is nonempty iff

`D_1<Ubar_2`,

which is equivalent to

`q_1<2q_2`.

Thus host-quality heterogeneity by itself does **not** produce a unique low-quality location. It creates a coordination region in which both a socially preferred high-quality volunteer equilibrium and a socially inferior low-quality volunteer equilibrium coexist.

The low-quality equilibrium has a real welfare loss, not merely a transfer loss:

`W_1(F)-W_2(F)=2E Delta_q`.

### 8.4 Mixed volunteer equilibrium in the mislocation region

In the strict region

`D_1<F<Ubar_2`,

neither jurisdiction wants to steal the trial once the other funds it, but both prefer funding to no trial. Reduce actions to `fund F` / `wait`.

Let

`A_i=q_i E+H-kF>0`.

Let `p_1` be the probability jurisdiction 1 funds and `p_2` the probability jurisdiction 2 funds. Indifference yields

`p_1=2A_2/(A_2+q_1E)`,

`p_2=2A_1/(A_1+q_2E)`.

The exact difference is

`p_2-p_1 = 2E(q_1-q_2)/[E(q_1+q_2)+H-kF] >0`.

Hence the lower-information jurisdiction funds more frequently in the completely mixed equilibrium. Since ties are split symmetrically, the difference in unconditional hosting probabilities is also

`P(host 2)-P(host 1)=p_2-p_1>0`.

This is a coordination/mixed-equilibrium result, not a unique-location prediction.

### 8.5 No local trial

If

`F>Ubar_1`,

neither jurisdiction is willing to cover the financing gap unilaterally; the decentralized outcome is no trial.

A planner still wants the high-quality trial if

`F<S_1`.

Thus the strict under-experimentation interval is

`Ubar_1<F<S_1`,

with width

`S_1-Ubar_1=q_1E/k`.

## 9. Revised Stage 4 regime logic

For `q_1>q_2`, the high-quality-host equilibrium has the following economically distinct regions.

### Private launch: F<=0

Trial additionality is zero. The limiting host subsidy is

`s_1^D=max{D_2,0}`.

Hence Stage 4's always-positive private-launch subsidy is weakened:

- if `H>E Delta_q`, positive host competition survives but is smaller than `H/k`;
- if `H<=E Delta_q`, information quality fully disciplines the lower-quality bidder and the limiting subsidy is zero.

When `D_2>0`, the fiscal welfare loss relative to zero-subsidy private launch is

`mu D_2`.

### Support needed: 0<F<Ubar_1

The high-quality-host subsidy is

`s_1^D=max{F,D_2}`.

If `F<D_2`, there is overpayment and supplier rent `D_2-F`; if `F>=D_2`, the high-quality equilibrium finances only the gap `F`.

### Under-experimentation

`Ubar_1<F<S_1`.

### Efficient no-trial

`F>=S_1`.

A low-quality volunteer equilibrium additionally exists in the coordination subregion `D_1<F<Ubar_2` when `q_1<2q_2`.

## 10. Stage 4 nesting / reduction tests

### q_1=q_2=1

`D_1=D_2=H/k`,

`Ubar_1=Ubar_2=(E+H)/k`,

`S_1=(2E+H)/k`.

This is exactly the Stage 4 threshold structure. The asymmetric epsilon-grid limit converges to the Stage 4 common bid `H/k`.

More generally `q_1=q_2=q` is Stage 4 with `E` rescaled to `qE`.

### E -> 0

`D_1,D_2 -> H/k`; all `q_i` effects disappear. Therefore `q_i` acts only through experimental information, not through generic site quality.

### H -> 0

`D_2=-E Delta_q/k<0`. The low-quality jurisdiction has no reason to contest the high-quality host; the host-rent bidding component disappears.

### V -> 0

`F -> C>0`; the privately viable zero-additionality region disappears.

### mu -> 0

Pure transfer overpayment ceases to create aggregate fiscal loss, but a low-quality volunteer equilibrium—when it exists—still loses `2E Delta_q` in real information value.

### q_1/q_2 -> 1

The information-quality term in `D_i` vanishes continuously and the Stage 4 symmetric structure is recovered.

## 11. Candidate-proposition status before prior-art kill

- **P5.1 Information-sensitive hosting bid:** mathematically **PROVED**.
- **P5.2 Local vs social information valuation:** mathematically **PROVED**; a jurisdiction internalizes `E Delta_q` of the `2E Delta_q` social location gain.
- **P5.3 Mislocation:** **PROVED ONLY AS EQUILIBRIUM POSSIBILITY / MIXED-STRATEGY POSITIVE PROBABILITY**, not as unique prediction.
- **P5.4 Wasteful competition with information quality:** **PROVED IN QUALIFIED FORM**; `q` can shrink or eliminate overpayment, and low-quality volunteer coordination can create real information loss.
- **P5.5 Governance implication:** mathematical benchmark exists, but novelty requires the Stage 5 prior-art kill.

The next question is not whether these formulas are correct; it is whether they are a genuinely new mechanism rather than a relabeled auction-with-externalities / asymmetric-volunteer model.
