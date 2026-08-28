# Stage 4 Verification Record

## Environment

- Python: 3.13.5
- SymPy: 1.14.0
- Random seed: `20260828`
- Verification script: `code/stage4_c4_verify.py`

## Symbolic checks

Declared composite notation:

- `k=1+mu`
- `T_H=H/k`
- `T_L=(E+H)/k`
- `T_S=(2E+H)/k`

Exact identities verified with SymPy:

- `T_L-T_H = E/k`
- `T_S-T_L = E/k`
- equilibrium host bid `s*=H/k`
- minimum-support welfare `W^N=2E+H-kF`
- decentralized bidding welfare `W^D=2E+H-F-mu H/k`
- in `0<F<T_H`, `W^N-W^D=mu(H/k-F)`
- volunteer mixed funding probability `q=2(E+H-kF)/(2E+H-kF)`
- mixed trial probability `4E(E+H-kF)/(2E+H-kF)^2`

## SOC / Hessian

`NOT APPLICABLE`.

The model is a discrete participation/location choice for the supplier and a linear host-subsidy bidding game. There is no smooth interior optimization problem whose FOC/SOC or Hessian characterizes equilibrium. Equilibrium is verified by unilateral-deviation inequalities and boundary analysis instead.

## Feasibility and participation

Supplier participation condition:

`max{s_1,s_2} >= F` for `F>0`; automatic if `F<=0`.

Government willingness conditions:

- outbid an already-funding rival only while `s<H/k`;
- unilaterally cover the financing gap only while `F<(E+H)/k`.

All equilibrium subsidies are nonnegative.

## Boundary cases

- `F=T_H`: symmetric and asymmetric weak equilibria coexist; no strict result uses the equality.
- `F=T_L`: a unilateral funder is indifferent to no trial; both trial and no-trial weak equilibria can arise.
- `F=T_S`: planner is indifferent between trial/no trial.
- `E=0`: under-experimentation interval collapses.
- `H=0`: hosting-race interval collapses.
- `mu=0`: excess subsidy is a transfer rather than a strict global welfare loss.

## Numerical region audit

Purpose: stress-test the analytical region inequalities and search for counterexamples.

Parameter ranges:

- `E ~ U[0.01,5]`
- `H ~ U[0.01,5]`
- `mu ~ U[0.01,2]`
- `C ~ U[0.1,10]`
- `V ~ U[0,12]`

Raw draws: 200,000.

All draws are economically admissible under the primitive nonnegativity assumptions; `F=C-V` is allowed to be negative because that represents private trial viability.

Region counts:

| Region | Count |
|---|---:|
| Private trial + hosting race | 115,706 |
| Support-needed bidding war | 20,633 |
| Minimum local support | 17,359 |
| Under-experimentation | 12,626 |
| No-trial efficient | 33,676 |

Counterexamples to the analytical sign/welfare claims: **0**.

## Volunteer mixed-equilibrium audit

10,000 additional draws were sampled from the strict volunteer region `T_H<F<T_L`.

For every draw:

- `0<q<1`;
- the expected payoff from funding equals the expected payoff from waiting to numerical tolerance `1e-10`.

Failures: **0**.

## Proof status table

| Result | Symbolic identity | Feasibility | Counterexample audit | Status |
|---|---|---|---|---|
| Threshold ordering | exact | yes | yes | `PROVED` |
| Bidding-war bid `H/k` | deviation proof | yes | grid/region checks | `PROVED` |
| Volunteer pure equilibria | deviation proof | yes | checked | `PROVED` |
| Volunteer mixed probability | exact | yes | 10k audit | `PROVED` |
| Zero-additionality for `F<=0` | exact | yes | yes | `PROVED` |
| Excess-welfare loss with `mu>0` | exact | yes | yes | `PROVED` |
| Under-experimentation interval | exact | yes | yes | `PROVED` |
| Mislocation | not in model | N/A | N/A | `NOT GENERATED` |
| Distinctness from ordinary location bidding | reduction test fails partially | N/A | literature re-check | `UNRESOLVED / BLOCKER` |

## Artefact audit

- closed forms in `REPORT.md` match the verification script;
- no numerical result is presented as proof;
- no persistent local ecosystem rent was inserted;
- no local private information or extra Stage 3 mechanism was added;
- the strongest negative result is retained: the information externality is separable from the hosting auction in the baseline.
