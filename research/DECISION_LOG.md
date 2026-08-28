# Decision Log

## Run metadata

- Run opened: 2026-08-28
- Canonical workflow commit at run start: `d5c5146098d97279ad3e90342fa757f0f31c8264`
- Repository bootstrap commits: `6091a064070655e640e1f80c5c04b76853381721`, `199170a3848c274c06eb5349c116ce8fed325e49`
- Stage 0–3 branch: `research/stage0-3-agentic-scouting`
- Stage 4 branch: `research/stage4-c4-minimal-model`
- Stage 5 branch: `research/stage5-c4-information-quality`

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
- **Major findings:** generic learning free riding, self-discovery/imitation, early-adopter externality, decentralized experimentation, local-information federalism, generic subsidy competition, public demonstration and supplier commercialization are occupied by close prior art.
- **Killed claims:** M1/M2/M3/M5/M6 as main contributions; M4 as label-level supplier novelty; M7 downgraded; M8 background/robustness.
- **Strongest prior-art threats:** Callander & Harstad (2015); Acemoglu, Bimpikis & Ozdaglar (2011); Chiappinelli, Giuffrida & Spagnolo (2025); Hausmann & Rodrik (2003); Detragiache (1998).
- **Surviving white space:** possible interaction among decentralized host incentives, supplier downstream commercialization, local host benefits and follower information/adoption benefits.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MECHANISM SEARCH`
- **Completion commit:** `0ec79ff91c260b60265e908befeca68ec117da20`

## Stage 3

- **Date:** 2026-08-28
- **Major findings:** eleven candidates generated; TOP 3 C4, C6, C3.
- **Preferred candidate:** C4 — competition to host a supplier’s scarce launch trial.
- **Strongest referee attack:** C4 may collapse to ordinary bidding for a mobile firm.
- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MINIMAL MODEL`
- **Mandatory status:** human approval required before Stage 4.
- **Completion commit:** `b9c010331235e3b74a4f68ec663cc7c8082b69c5`

## Stage 4 — C4 Minimal Model Gate

- **Date:** 2026-08-28
- **Human authorization:** C4 explicitly approved.
- **Branch:** `research/stage4-c4-minimal-model`
- **Model:** two symmetric jurisdictions, one supplier, one launch trial; `F=C-V`, information benefit `E`, host-only benefit `H`, excess burden `mu`.
- **Thresholds:** `T_H=H/(1+mu)`, `T_L=(E+H)/(1+mu)`, `T_S=(2E+H)/(1+mu)`.
- **Proved:** zero-additionality subsidy at `F<=0`; overpayment for `0<F<T_H`; productive pure volunteer support for `T_H<F<T_L`; under-experimentation for `T_L<F<T_S`; efficient no trial above `T_S`.
- **Negative finding:** symmetric model cannot generate mislocation.
- **Verification:** exact SymPy; 200,000 region/welfare draws zero violations; 10,000 volunteer checks zero failures.
- **Single blocker:** `E` host invariant, so information externality does not enter host bidding and C4 remains partly ordinary location bidding plus free riding.
- **Canonical verdict:** `CONDITIONAL GO`
- **Routing/status:** `GO TO STAGE 5 MECHANISM HARDENING`
- **Only authorized modification:** host-dependent information productivity `q_i`.
- **Completion commit:** `da8d4e25f2e0bedd2832748407c01a5b01d12f28`

## Stage 5 — C4 Host-Dependent Information Quality Hardening

- **Date:** 2026-08-28
- **Branch:** `research/stage5-c4-information-quality`
- **Authorized change used:** exactly one new primitive `q_i>0`, information/learning quality of a trial hosted in jurisdiction i. No second substantive mechanism was added.
- **Stage 4 blocker status:** **RESOLVED MATHEMATICALLY**. If `q_1>q_2`, the low-quality jurisdiction's maximum contest bid is `D_2=[H-E(q_1-q_2)]/(1+mu)`, so the information produced at the rival host changes the loser's outside option and bidding willingness.
- **Other exact results:** high-quality local threshold `Ubar_1=(q_1E+H)/(1+mu)`; social threshold `S_1=(2q_1E+H)/(1+mu)`; information quality can reduce/eliminate the private-launch host race; low-quality volunteer equilibrium exists only in the coordination region `D_1<F<Ubar_2`, nonempty iff `q_1<2q_2`.
- **Mislocation finding:** no unique low-q mislocation in the active contest; low-q hosting appears only through pure-equilibrium multiplicity / positive probability in the asymmetric volunteer mixed equilibrium.
- **Verification:** exact SymPy identities; 300,000 feasible random draws, zero analytical violations; 11,364 draws with a low-q volunteer/mislocation equilibrium; zero mixed-equilibrium violations.
- **Prior-art result:** the successful q_i feedback maps directly to auctions with identity-dependent externalities (Jehiel, Moldovanu & Stacchetti 1999; Jehiel & Moldovanu 2000). Other blocks remain close to Slattery/Mast local subsidy competition, Callander–Harstad heterogeneous experimentation, external-validity site selection, and volunteer-dilemma theory.
- **Key research conclusion:** the single allowed modification solves the algebraic defect but reveals that the hardened mechanism is structurally known. Escaping that class would require a second substantive repair, prohibited by Stage 5 governance.
- **Canonical verdict:** `NO-GO`
- **Routing/status:** `C4 TERMINATED AT STAGE 5`
- **Stage 6:** `NOT AUTHORIZED / NOT EXECUTED`
- **C6/C3:** remain frozen; no automatic pivot.
- **Model/verification commit:** `22a50c29e2ba92493bfccb5af469bf81ddc395d5`
- **Prior-art/referee verdict commit:** `a2fdc79760337371ed1a8e462d075b2ac9249023`
- **Completion metadata commit:** `TO_BE_BACKFILLED_AFTER_STAGE_5_METADATA_COMMIT`
