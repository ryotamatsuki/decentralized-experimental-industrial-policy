# Decentralized Experimental Industrial Policy

This repository records a stage-gated theory-research project on decentralized government support for private-technology experimentation.

The motivating institution is the class of programs exemplified by Triangle Ehime. Triangle Ehime is a source of institutional facts and potentially meaningful frictions; it is not the intended object of the final theory.

## Current status

**Stage 4 Minimal Model Gate has been completed for C4.**

- Stage 0: `GO` → `GO TO AUDIT`
- Stage 1: `GO` → `GO TO NOVELTY GATE`
- Stage 2: `GO` → `GO TO MECHANISM SEARCH`
- Stage 3: `GO` → `GO TO MINIMAL MODEL`
- Stage 4 C4: **`CONDITIONAL GO` → `GO TO STAGE 5 MECHANISM HARDENING`**
- Stage 5: **NOT EXECUTED**

The Stage 4 baseline mathematically separates the supplier's experiment-occurrence margin from local host-location bidding and proves regions of zero-additionality subsidy, overpayment, productive local support, and decentralized under-experimentation. However, the information externality is host-invariant and remains separable from the hosting auction. This prevents a direct Stage 6 novelty re-kill.

Canonical workflow: [`ryotamatsuki/research-paper-workflow`](https://github.com/ryotamatsuki/research-paper-workflow).

## Stage 4 baseline

Define:

- `F=C-V`: trial cost net of supplier downstream commercialization value;
- `E`: per-jurisdiction information/adoption benefit from any trial;
- `H`: host-only local benefit;
- `mu`: marginal excess burden of public finance.

The three exact thresholds are

- `T_H = H/(1+mu)` — host-bidding threshold;
- `T_L = (E+H)/(1+mu)` — local unilateral-financing threshold;
- `T_S = (2E+H)/(1+mu)` — social financing threshold.

The model yields:

1. `F<=0`: the supplier would conduct the trial privately, yet local governments bid positively for host status; experimentation additionality is zero.
2. `0<F<T_H`: support is needed but local bidding exceeds the financing gap and creates supplier rent.
3. `T_H<F<T_L`: pure volunteer equilibria fund exactly the gap.
4. `T_L<F<T_S`: decentralized governments do not fund a socially valuable trial.
5. `F>=T_S`: no support/no trial is efficient.

The 200,000-draw numerical audit found zero violations of the analytical region/welfare conditions.

## Stage 4 blocker

The strongest Stage 3 objection survives in a narrower form: the non-additionality/rent-transfer result remains close to ordinary local competition for mobile firms. Slattery (2025) and Mast (2020) materially strengthen this prior-art threat.

The single authorized Stage 5 change is therefore:

> replace host-invariant information value with one host-dependent information-productivity primitive `q_i` and test whether the information-producing nature of the trial changes the host-location competition itself.

Everything else remains frozen. C6, C3, dynamics, private information, endogenous disclosure, political credit, persistent ecosystem rents, and multiple suppliers are not authorized as C4 rescue mechanisms.

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
- [`research/stage-02/CLOSEST_PAPER_MATRIX.md`](research/stage-02/CLOSEST_PAPER_MATRIX.md)
- [`research/stage-03/REPORT.md`](research/stage-03/REPORT.md)
- [`research/stage-03/STAGE4_HANDOFF.md`](research/stage-03/STAGE4_HANDOFF.md)
- [`research/stage-04/REPORT.md`](research/stage-04/REPORT.md)
- [`research/stage-04/MODEL.md`](research/stage-04/MODEL.md)
- [`research/stage-04/VERIFICATION.md`](research/stage-04/VERIFICATION.md)
- [`research/stage-04/NEXT_STAGE_CONTRACT.md`](research/stage-04/NEXT_STAGE_CONTRACT.md)

### Reproducibility

- [`code/stage4_c4_verify.py`](code/stage4_c4_verify.py)
- [`code/requirements-stage4.txt`](code/requirements-stage4.txt)
- [`bibliography/references.bib`](bibliography/references.bib)

## Hard rule

Stage 5 may change only the one primitive authorized in `research/stage-04/NEXT_STAGE_CONTRACT.md`. If that modification does not make the experiment-information mechanism feed back into host competition, C4 must be terminated rather than rescued through feature accumulation.
