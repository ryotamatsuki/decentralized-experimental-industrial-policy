# Decentralized Experimental Industrial Policy

This repository records a stage-gated theory-research project on decentralized government support for private-technology experimentation. Triangle Ehime is an institutional motivation, not the intended object of the final theory.

## Current status

**Stage 5 Mechanism Hardening has been completed for C4, and C4 is terminated.**

- Stage 0: `GO` → `GO TO AUDIT`
- Stage 1: `GO` → `GO TO NOVELTY GATE`
- Stage 2: `GO` → `GO TO MECHANISM SEARCH`
- Stage 3: `GO` → `GO TO MINIMAL MODEL`
- Stage 4 C4: `CONDITIONAL GO` → `GO TO STAGE 5 MECHANISM HARDENING`
- Stage 5 C4: **`NO-GO` → C4 TERMINATED**
- Stage 6 for C4: **NOT AUTHORIZED / NOT EXECUTED**

Canonical workflow: [`ryotamatsuki/research-paper-workflow`](https://github.com/ryotamatsuki/research-paper-workflow).

## What Stage 4 established

With `F=C-V`, information benefit `E`, host-only benefit `H`, and public-finance excess burden `mu`, Stage 4 derived

- `T_H=H/(1+mu)`;
- `T_L=(E+H)/(1+mu)`;
- `T_S=(2E+H)/(1+mu)`.

The symmetric minimal model proved regions of zero-additionality local subsidy, overpayment, productive local volunteer support, decentralized under-experimentation, and efficient no-trial. Its single blocker was that information value was host invariant and therefore did not enter the host-location competition.

## What Stage 5 changed

Stage 5 added exactly one authorized primitive:

`q_i>0` — the generalizable information/learning quality of a trial when jurisdiction `i` hosts.

If `q_1>q_2`, the lower-quality jurisdiction's maximum willingness to take hosting from the high-quality jurisdiction becomes

`D_2=[H-E(q_1-q_2)]/(1+mu)`.

Thus better experimental information improves the loser's outside option and directly reduces its host bid. If `E(q_1-q_2)>=H`, the lower-quality jurisdiction has no positive willingness to pay merely to steal the trial.

The modification therefore **solved the Stage 4 algebraic blocker**.

## Why C4 is nevertheless NO-GO

The hardening exposed a stronger novelty problem.

The Stage 5 hosting game is structurally an **auction/allocation problem with identity-dependent externalities**: a jurisdiction that loses is not indifferent about which rival hosts, because host identity determines the evidence it receives. This strategic structure is covered by the auction-with-externalities literature (Jehiel, Moldovanu & Stacchetti 1999; Jehiel & Moldovanu 2000).

Other blocks also remain close to established theory:

- local subsidy/rent competition: Slattery (2025), Mast (2020);
- heterogeneous experimentation and information spillovers: Callander & Harstad (2015);
- experimental-site/external-validity choice: Gechter et al.;
- volunteer/multiple-equilibrium provision: Myatt & Wallace (2008), Kawagoe et al. (2023).

`q_i` does not mechanically impose a low-quality location. The active contest selects the high-q site. A low-q host appears only through volunteer-equilibrium multiplicity / mixed provision, which is itself close to existing volunteer-dilemma logic.

Under the project governance, escaping these prior-art classes would require a second substantive repair, which is prohibited. C4 is therefore terminated rather than feature-accumulated.

## Reproducibility

- Stage 4: [`code/stage4_c4_verify.py`](code/stage4_c4_verify.py)
- Stage 5: [`code/stage5_c4_q_verify.py`](code/stage5_c4_q_verify.py)

Stage 5 used exact SymPy checks and a 300,000-draw diagnostic counterexample audit with zero violations of the reported analytical conditions. Numerical results are not treated as proofs.

## Navigation

### Governance / project state

- [`RESEARCH_CHARTER.md`](RESEARCH_CHARTER.md)
- [`research/DECISION_LOG.md`](research/DECISION_LOG.md)
- [`research/CLAIM_EVIDENCE_LEDGER.md`](research/CLAIM_EVIDENCE_LEDGER.md)
- [`research/REJECTED_BRANCHES.md`](research/REJECTED_BRANCHES.md)

### Stage reports

- [`research/stage-00/REPORT.md`](research/stage-00/REPORT.md)
- [`research/stage-01/REPORT.md`](research/stage-01/REPORT.md)
- [`research/stage-02/REPORT.md`](research/stage-02/REPORT.md)
- [`research/stage-03/REPORT.md`](research/stage-03/REPORT.md)
- [`research/stage-04/REPORT.md`](research/stage-04/REPORT.md)
- [`research/stage-05/REPORT.md`](research/stage-05/REPORT.md)
- [`research/stage-05/MODEL_HARDENING.md`](research/stage-05/MODEL_HARDENING.md)
- [`research/stage-05/VERIFICATION.md`](research/stage-05/VERIFICATION.md)
- [`research/stage-05/PRIOR_ART_RECHECK.md`](research/stage-05/PRIOR_ART_RECHECK.md)
- [`research/stage-05/REFEREE_ATTACK.md`](research/stage-05/REFEREE_ATTACK.md)
- [`research/stage-05/NEXT_STAGE_CONTRACT.md`](research/stage-05/NEXT_STAGE_CONTRACT.md)

## Hard rule after Stage 5

Do not route C4 to Stage 6 and do not add another mechanism to rescue it. If research continues, return to the Stage 3 human hard gate; C6 or C3 requires a separate explicit human decision and a new branch.
