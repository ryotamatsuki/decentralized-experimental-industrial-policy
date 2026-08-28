# Decision Log

## Run metadata

- Run opened: 2026-08-28
- Canonical workflow commit at initial run start: `d5c5146098d97279ad3e90342fa757f0f31c8264`
- Repository bootstrap commits: `6091a064070655e640e1f80c5c04b76853381721`, `199170a3848c274c06eb5349c116ce8fed325e49`
- Stage 0–3 branch: `research/stage0-3-agentic-scouting`
- Stage 4 branch: `research/stage4-c4-minimal-model`
- Stage 5 branch: `research/stage5-c4-information-quality`
- Stage 3 re-entry branch: `research/stage3-reentry-c6-c3-rekill`

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
- **Proved:** zero-additionality subsidy, overpayment, productive local volunteer support, under-experimentation, and efficient no-trial regions.
- **Negative finding:** symmetric model cannot generate mislocation.
- **Single blocker:** information benefit host invariant, so information externality does not enter host bidding.
- **Canonical verdict:** `CONDITIONAL GO`
- **Routing/status:** `GO TO STAGE 5 MECHANISM HARDENING`
- **Only authorized modification:** host-dependent information productivity `q_i`.

## Stage 5 — C4 Host-Dependent Information Quality Hardening

- **Date:** 2026-08-28
- **Branch:** `research/stage5-c4-information-quality`
- **Authorized change used:** exactly one new primitive `q_i>0`.
- **Stage 4 blocker:** resolved mathematically; evidence quality changes the losing jurisdiction's outside option and bidding willingness.
- **Prior-art result:** hardened structure maps into auctions with identity-dependent externalities; other blocks remain close to subsidy competition, heterogeneous experimentation and volunteer-provision theory.
- **Canonical verdict:** `NO-GO`
- **Routing/status:** `C4 TERMINATED AT STAGE 5`
- **Stage 6:** `NOT AUTHORIZED / NOT EXECUTED`
- **C6/C3:** frozen pending explicit human Stage 3 re-entry.
- **Final Stage 5 head before re-entry:** `319fa6991f7a384f8954975a57bc425712df9a05`

## Stage 3 Re-Entry — C6 vs C3 Targeted Novelty Re-Kill

- **Date:** 2026-08-28
- **Human authorization:** explicit Stage 3 re-entry request limited to C6 and C3.
- **Branch:** `research/stage3-reentry-c6-c3-rekill`
- **C4 status:** `TERMINATED / FROZEN`; no C4 hybrid or rescue considered.
- **C6 main finding:** the admissible core game is supplier/sender-chosen test/evidence design followed by downstream acceptance/certification. DeMarzo–Kremer–Skrzypacz (2019), Shishkin (2026), Weksler–Zik (2022) and adjacent test-design theory materially contain or closely overlap the loop. Removing the public sponsor leaves the mechanism intact; making the sponsor essential would require another payoff/instrument.
- **C6 verdict:** `NO-GO`.
- **C6 targeted re-kill commit:** `9e5589ea7a15ff7cfcaaec91b10d3f87c66350b8`.
- **C3 main finding:** a one-process learning formulation can distinguish supplier-appropriable learning from public spillovers, but the minimum theory becomes the classic private-versus-social learning/appropriability wedge. Nemet (2012), Irwin–Klenow (1994), Foster–Rosenzweig (1995), Glachant–Ménière (2013) and current learning-by-deploying work are strong threats. A distinct feedback requires an additional mechanism.
- **C3 verdict:** `NO-GO`.
- **C3 targeted re-kill commit:** `27780444553ce62d8c50dbe0fff6906323d1fbce`.
- **Head-to-head/referee result:** neither candidate independently satisfies Stage 3 success criteria; fatal prior art overrides equal screening scores.
- **Final selection:** **`BOTH NO-GO`**.
- **Selection/report commit:** `d395b52f009a56e671e673d162c4ebbb654e726c`.
- **Canonical verdict:** `NO-GO`.
- **Any new Stage 4:** `NOT AUTHORIZED / NOT EXECUTED`.
- **Next route:** human decision required between a genuinely fresh Stage 3 mechanism search under all accumulated kills or return to Stage 0 for research-question reframing.
- **Stop:** `STOPPED AFTER STAGE 3 RE-ENTRY — HUMAN APPROVAL REQUIRED BEFORE ANY NEW STAGE 4`.
