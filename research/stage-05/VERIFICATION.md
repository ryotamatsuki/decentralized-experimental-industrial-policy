# Stage 5 Verification — C4 with Host-Dependent Information Quality

## Environment

- Python / SymPy verification required by the canonical Stage 5 contract.
- Stage 4 verification file is preserved unchanged.
- New verification script: `code/stage5_c4_q_verify.py`.
- Random seed: `20260828`.

## 1. Symbolic identities

For `k=1+mu`, `Delta_q=q_1-q_2`, define

`D_1=(H+E Delta_q)/k`,

`D_2=(H-E Delta_q)/k`,

`Ubar_1=(q_1E+H)/k`,

`Ubar_2=(q_2E+H)/k`,

`S_1=(2q_1E+H)/k`.

Exact SymPy checks verify:

- `D_1-D_2 = 2E Delta_q/k`;
- `D_1+D_2 = 2H/k`;
- `Ubar_1-D_1 = q_2E/k`;
- `Ubar_2-D_2 = q_1E/k`;
- `Ubar_2-D_1 = E(2q_2-q_1)/k`;
- `S_1-Ubar_1 = q_1E/k`;
- high-vs-low host welfare difference at equal subsidy is `2E Delta_q`.

These checks establish the exact local/social wedges used in the analytical report.

## 2. Stage 4 nesting

At `q_1=q_2=1`:

- `D_1=D_2=H/k=T_H`;
- `Ubar_1=Ubar_2=(E+H)/k=T_L`;
- `S_1=(2E+H)/k=T_S`.

Thus the Stage 5 model nests Stage 4 exactly.

For common `q_1=q_2=q`, it nests Stage 4 after the harmless rescaling `E_stage4=qE`.

## 3. Information-sensitive host bidding

The lower-quality region's contest value satisfies

`D_2=H/k-E Delta_q/k`.

SymPy verifies

`d D_2/d Delta_q = -E/k <0`.

The contest value is nonpositive exactly when

`E Delta_q >= H`.

Hence a sufficiently informative high-quality site eliminates the low-quality jurisdiction's willingness to pay merely to take hosting away from that site.

Reduction `E=0` gives `D_2=H/k`, proving that the `q` term is not a generic site-quality effect independent of experimentation.

## 4. Volunteer/mislocation region

A low-quality-host pure equilibrium requires

`D_1<F<Ubar_2`.

The interval is nonempty iff

`D_1<Ubar_2`,

and SymPy reduces this exactly to

`q_1<2q_2`.

At the same minimum subsidy `F`, the welfare loss of the low-quality host is

`2E(q_1-q_2)>0`.

This is a real information loss and survives `mu=0`.

## 5. Mixed volunteer equilibrium

In `D_1<F<Ubar_2`, define

`A_i=q_iE+H-kF`.

The funding probabilities are

`p_1=2A_2/(A_2+q_1E)`,

`p_2=2A_1/(A_1+q_2E)`.

SymPy factors the difference as

`p_2-p_1 = 2E(q_1-q_2)/[E(q_1+q_2)+H-kF]`.

The region restrictions imply the denominator is positive, so `p_2>p_1`. With symmetric tie breaking, `P(host 2)-P(host 1)=p_2-p_1` exactly.

Numerical checks verify both players' fund/wait indifference identities.

## 6. Planner and under-experimentation

High-quality social threshold:

`S_1=(2q_1E+H)/k`.

High-quality local volunteer threshold:

`Ubar_1=(q_1E+H)/k`.

The strict decentralized under-experimentation interval has width

`S_1-Ubar_1=q_1E/k>0`.

This is analytically the same externality logic as Stage 4, scaled by host information quality.

## 7. Fiscal-overpayment check

For `F>0` and `F<D_2`, the high-quality host wins in the vanishing-bid-grid limit at subsidy `D_2`, rather than the minimum supplier gap `F`.

Supplier excess rent is

`D_2-F>0`.

Relative to minimum support at the same high-quality site, aggregate fiscal loss is

`mu(D_2-F)>0`.

For `F<=0` and `D_2>0`, trial additionality is zero and the local subsidy creates fiscal loss

`mu D_2>0`.

When `D_2<=0`, this private-launch host-race payment collapses to zero in the vanishing-grid limit.

## 8. Numerical counterexample audit

Sampling ranges:

- `E ~ U[0.01,5]`;
- `H ~ U[0.01,5]`;
- `mu ~ U[0.01,2]`;
- `C ~ U[0.1,10]`;
- `V ~ U[0,12]`;
- two raw quality draws independently `U[0.2,2.5]`, ordered as `q_1=max`, `q_2=min`.

Raw / feasible draws: **300,000 / 300,000**.

Mutually exclusive main-region counts:

- private launch, uncontested because `D_2<=0`: **62,074**;
- private launch, positive host contest: **112,083**;
- support-needed contested overpayment (`0<F<D_2`): **16,164**;
- high-quality minimum-support region: **54,158**;
- decentralized under-experimentation: **20,336**;
- no-trial efficient: **35,185**.

These sum to 300,000.

The low-quality pure volunteer/mislocation equilibrium existed in **11,364** draws (overlapping the minimum-support class), confirming a positive-measure coordination region.

Counterexample results:

- analytical region/sign violations: **0**;
- mixed-strategy probability/indifference violations: **0**;
- failures of `q_1<2q_2` in the strict mislocation interval: **0**;
- failures of `P(host 2)>P(host 1)` in the completely mixed mislocation region: **0**.

Numerical evidence is diagnostic only; all reported theorem candidates are based on exact inequalities.

## 9. Mandatory reduction audit

- `q_1=q_2=1`: exact Stage 4 recovery — **PASS**.
- `E->0`: quality effect disappears from bids — **PASS**.
- `H->0`: host-rent contest disappears; `D_2<0` for unequal qualities — **PASS**.
- `V->0`: clean private-launch region disappears — **PASS**.
- `mu->0`: transfer/excess-burden losses disappear while real mislocation loss remains — **PASS**.
- `q_1/q_2->1`: quality term in contest values converges continuously to zero — **PASS**.

## 10. Mathematical verification verdict

The one authorized modification **does resolve the narrow Stage 4 algebraic blocker**: `q_i` enters the losing payoff and therefore directly changes hosting willingness and equilibrium payments.

However, mathematical success is not the Stage 5 research verdict. Prior-art analysis must determine whether this is simply a known auction with identity-dependent externalities plus a reserve/volunteer region.
