# Decision Log

## Run metadata

- Run opened: 2026-08-28
- Canonical workflow commit at run start: `d5c5146098d97279ad3e90342fa757f0f31c8264`
- Repository bootstrap commits: `6091a064070655e640e1f80c5c04b76853381721`, `199170a3848c274c06eb5349c116ce8fed325e49`
- Stage 0–3 branch: `research/stage0-3-agentic-scouting`
- Stage 4 branch: `research/stage4-c4-minimal-model`

## Stage 0

- **Date:** 2026-08-28
- **Major findings:** a researchable strategic and welfare question exists; eight candidate mechanisms were separated without constructing a model.
- **Killed claims:** Triangle Ehime as standalone contribution; presumption local intervention is beneficial; first-mover + free riding as novelty by itself; omnibus model.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO AUDIT`
- **Completion commit:** `74baaa33c283b8c9711b07cd91724b6f13e5797f`

## Stage 1

- **Date:** 2026-08-28
- **Major findings:** a generalizable policy class is primary-source verified: public selection/matching, trial support, evidence production, diffusion/commercialization, and subnational/national institutional analogues.
- **Killed/bounded claims:** observed strategic cross-prefecture free riding; guaranteed persistent local first-mover rent; inherent local informational superiority; complete public absorption of failure risk; universal public ownership of project IP.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO NOVELTY GATE`
- **Completion commit:** `eaf41d029e82f6c98a7441e83060870275d7df8e`

## Stage 2

- **Date:** 2026-08-28
- **Major findings:** generic learning free riding, self-discovery/imitation, early-adopter externality, decentralized experimentation, local-information federalism, generic subsidy competition, public demonstration and supplier commercialization are all occupied by close prior art. The 2025 IJIO public-procurement-of-innovation survey materially raises the novelty bar for any government–supplier mechanism.
- **Killed claims:** M1/M2/M3/M5/M6 as main contributions; M4 as label-level supplier novelty; M7 downgraded to secondary/unresolved; M8 to robustness/background unless a distinct loop emerges.
- **Strongest prior-art threats:** Callander & Harstad (2015); Acemoglu, Bimpikis & Ozdaglar (2011); Chiappinelli, Giuffrida & Spagnolo (2025) and PPI theory; Hausmann & Rodrik (2003); Detragiache (1998).
- **Surviving white space:** a `POTENTIALLY NOVEL / UNRESOLVED` interaction separating decentralized host-government incentives, local host benefits, supplier downstream commercialization rents, and follower-jurisdiction informational/adoption benefits.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MECHANISM SEARCH`
- **Completion commit:** `0ec79ff91c260b60265e908befeca68ec117da20`

## Stage 3

- **Date:** 2026-08-28
- **Canonical inputs:** Stage 2 surviving white space, killed claims, closest-paper matrix and reduction tests.
- **Major findings:** eleven distinct strategic-loop candidates were generated and scored using pre-specified weights. TOP 3 are C4 host competition for a scarce supplier launch trial, C6 success-biased demonstration/certification, and C3 local-fit uncertainty × reusable supplier learning.
- **Preferred candidate:** **C4 — Competition to host a supplier’s scarce launch trial.** It separates the experiment extensive margin from the location/rent-shifting margin.
- **Strongest referee attack:** C4 may collapse to ordinary bidding for a mobile firm.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MINIMAL MODEL`
- **Mandatory status:** `STOPPED AFTER STAGE 3 — HUMAN APPROVAL REQUIRED BEFORE STAGE 4`
- **Completion commit:** `b9c010331235e3b74a4f68ec663cc7c8082b69c5`

## Stage 4 — C4 Minimal Model Gate

- **Date:** 2026-08-28
- **Human authorization:** explicit approval of C4 received before Stage 4 execution.
- **Branch:** `research/stage4-c4-minimal-model`
- **Canonical inputs:** Stage 3 C4 handoff; Stage 4 canonical template; symbolic/numerical verification checklists; frozen Stage 2 novelty kills.
- **Exact model:** two symmetric jurisdictions, one supplier, one launch trial; trial cost `C`, supplier downstream value `V`, financing gap `F=C-V`, per-jurisdiction information benefit `E`, host-only benefit `H`, excess burden `mu`, simultaneous host-contingent subsidy offers.
- **Main mathematical findings:** thresholds `T_H=H/(1+mu)`, `T_L=(E+H)/(1+mu)`, `T_S=(2E+H)/(1+mu)` partition hosting-race, volunteer-financing, decentralized no-trial, and social no-trial regions.
- **Proved results:** positive local subsidy with zero experimentation additionality when `F<=0`; overpayment relative to the financing gap when `0<F<T_H`; productive minimum-gap pure equilibria when `T_H<F<T_L`; under-experimentation when `T_L<F<T_S`; region-specific dominance of higher-level minimum-gap targeting.
- **Negative/limiting finding:** the symmetric baseline cannot generate mislocation.
- **Verification:** exact SymPy identities; 200,000-draw region/welfare audit with zero violations; 10,000-draw volunteer mixed-equilibrium indifference audit with zero failures.
- **Prior-art re-check:** Slattery (2025 JPE) and Mast (2020 AEJ: Applied) materially strengthen the ordinary mobile-firm bidding threat for the non-additionality/rent-transfer result.
- **Single diagnosed blocker:** the information externality `E` is host-invariant and does not enter the host bid `H/(1+mu)`; the hosting-auction and experimentation-externality wedges remain separable.
- **Canonical verdict:** `CONDITIONAL GO`
- **Routing/status:** `GO TO STAGE 5 MECHANISM HARDENING`
- **Authorized next change:** replace host-invariant information value with one host-dependent information-productivity primitive `q_i`; everything else frozen.
- **Stage 5 status:** **NOT EXECUTED**.
- **Completion commit:** `da8d4e25f2e0bedd2832748407c01a5b01d12f28`
