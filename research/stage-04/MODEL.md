# C4 Minimal Model — Exact Specification and Proof Map

## 1. Players and timing

Two symmetric local governments `i=1,2` and one private technology supplier.

1. Governments simultaneously announce host-contingent subsidy offers `s_i >= 0`.
2. Supplier observes offers and chooses `no trial`, `host 1`, or `host 2`.
3. A hosted trial produces downstream commercialization value for the supplier and information/adoption value for both regions.

Tie-breaking between equal offers is symmetric.

## 2. Primitives

- `C>0`: real trial cost.
- `V>=0`: supplier downstream commercialization value conditional on trial.
- `F=C-V`: supplier financing gap.
- `E>=0`: per-jurisdiction information/adoption benefit from any trial.
- `H>0`: incremental host-only benefit.
- `mu>0`: marginal excess burden of public funds.
- `k=1+mu`.

No private local information, political credit, multiple suppliers, persistent ecosystem rent, endogenous effort, disclosure choice, repeated interaction, or host-specific trial quality appears in the baseline.

## 3. Supplier problem

If jurisdiction `i` hosts, supplier payoff is

`Pi_S(i)=V+s_i-C=s_i-F`.

Hence a trial occurs iff

`max{s_1,s_2} >= F`

when `F>0`. If `F<=0`, a trial is privately viable even with zero subsidy.

Conditional on trial, supplier selects the highest offer.

## 4. Government payoff

If `i` hosts:

`U_i^H = E + H - k s_i`.

If the other jurisdiction hosts:

`U_i^N = E`.

If no trial occurs:

`U_i^0 = 0`.

The incremental willingness to outbid an already-funding rival is therefore governed by `H`, whereas willingness to volunteer when otherwise no trial occurs is governed by `E+H`.

## 5. Three thresholds

`T_H = H/k`

`T_L = (E+H)/k`

`T_S = (2E+H)/k`

For `E>0`:

`T_H < T_L < T_S`.

Interpretation:

- `T_H`: maximum host-location bid relative to losing an already-occurring trial;
- `T_L`: maximum financing gap one local government is willing to cover when otherwise no trial occurs;
- `T_S`: maximum financing gap worth covering from aggregate social welfare.

## 6. Proposition 1 — Pure-strategy equilibrium partition

### A. `F<T_H`

Claim: the unique pure equilibrium is `s_1=s_2=T_H`.

Proof sketch:

- A common bid `s<T_H` cannot be an equilibrium: a government can bid `s+epsilon`, win for sure, and obtain `E+H-k(s+epsilon)`, which exceeds its tie payoff for small `epsilon`.
- A common bid `s>T_H` cannot be an equilibrium: a government can underbid, lose, and receive `E`, which exceeds the negative incremental host payoff `H-ks`.
- At `s=T_H`, winning yields `E`, losing yields `E`, and any overbid gives less than `E`.
- No asymmetric pure equilibrium exists because a strict winner can reduce its bid while remaining the winner (or down to the participation threshold) unless the opponent is at the same limiting value.

Thus `s_1=s_2=T_H`.

### B. `T_H<F<T_L`

Since `F>T_H`, once the rival funds the trial, a government strictly prefers losing to outbidding. But since `F<T_L`, a government prefers funding `F` to no trial when the rival does not fund.

Therefore the pure equilibria are `(F,0)` and `(0,F)` up to outcome-equivalent inactive offers below `F`.

### C. `F>T_L`

Even the minimum inducing offer `F` gives a unilateral funder

`E+H-kF<0`.

Funding is therefore dominated by waiting/no offer in the reduced game. The unique equilibrium outcome is no trial.

Boundary equalities generate weak/multiple equilibria and are excluded from strict propositions.

## 7. Proposition 2 — Symmetric mixed equilibrium in the volunteer region

For `T_H<F<T_L`, reduce actions to `fund F` or `wait`.

Let `D=H-kF<0`. If the rival funds with probability `q`:

- funding payoff: `(1-q)(E+D)+q(E+D/2)`;
- waiting payoff: `qE`.

Indifference yields

`q = 2(E+D)/(2E+D)`

or

`q = 2(E+H-kF)/(2E+H-kF)`.

Because `T_H<F<T_L`, `0<q<1`.

The trial probability is

`1-(1-q)^2 = 4E(E+H-kF)/(2E+H-kF)^2`.

## 8. Proposition 3 — Welfare

Aggregate welfare if the trial occurs with host subsidy `s` is the sum of supplier and two local-government payoffs:

`W(s) = (s-F) + (E+H-ks) + E`

`= 2E+H-F-mu s`.

Thus transfers cancel except for the excess burden.

If `F>0`, a planner using the minimum inducing support `s=F` obtains

`W^N = 2E+H-kF`.

The social trial threshold is therefore `F<T_S`.

## 9. Proposition 4 — Non-additional subsidy and overpayment

### Private launch: `F<=0`

Without government, the trial occurs. Decentralized host competition still sets `s=T_H`.

Experiment additionality: `0`.

Welfare gap versus no-subsidy private launch:

`Delta W = mu T_H = mu H/k >0`.

### Support-needed bidding war: `0<F<T_H`

Minimum inducing support is `F`, but equilibrium support is `T_H`.

Supplier rent:

`R=T_H-F>0`.

Welfare loss relative to minimum-gap support:

`W^N-W^D = mu(T_H-F)>0`.

## 10. Proposition 5 — Under-experimentation

A local government refuses unilateral financing when

`F>T_L`.

A planner still prefers a trial when

`F<T_S`.

Hence for

`T_L<F<T_S`

decentralization yields no trial while the planner strictly prefers to induce one.

The interval width is

`T_S-T_L=E/k`.

## 11. Commercialization comparative static

Since `F=C-V`, raising `V` lowers `F` one-for-one.

Holding `E,H,mu,C` fixed, higher commercialization value moves the economy through:

`no socially valuable trial -> under-experimentation -> minimum local support -> bidding-war overpayment -> privately viable trial with non-additional local subsidy`.

In the overpayment region,

`d(T_H-F)/dV=1`.

Thus the amount of the local subsidy that is pure supplier rent rises as the supplier becomes more privately capable of financing the experiment.

## 12. Reduction tests

- `E=0`: `T_L=T_S=T_H`; under-experimentation disappears, host bidding remains.
- `H=0`: `T_H=0`; host bidding/rent shifting disappears, leaving a standard financing/free-rider problem.
- `V=0`: `F=C>0`; the clean private-launch/zero-additionality region disappears.
- `mu=0`: strict global welfare loss from transfers disappears.

These reductions show that each primitive has a role, but they also expose that the roles remain separable in the baseline.
