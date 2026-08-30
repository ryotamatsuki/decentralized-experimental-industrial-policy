# Cycle 1 Re-Audit — Final Report

## 1. Executive verdict

# **RE-AUDIT CONFIRMS OLD NO-GO**

The re-audit found a real institutional distinction that the old audit compressed too aggressively:

- procurement-stage entry is not the same as post-procurement complementor entry;
- lotting is not the same instrument as interoperability;
- public procurement can include technical, interface, data-right, portability, and lifecycle-support terms that affect a deployed system after award.

But this correction does not yield a surviving theory theme. Once the distinction is kept, the proposed strategic mechanisms reduce to existing procurement, dynamic-competition, platform-openness, compatibility, switching-cost, vertical-foreclosure, hold-up, and supplier-investment models. Six minimal variants were tested; none met the Stage 3 threshold and none escaped a fatal reduction. Stage 4 was therefore not run.

This result confirms the old NO-GO conclusion while correcting its incomplete rationale.

## 2. What the old Cycle 1 did correctly

The old audit correctly recognized that:

1. bundle versus separate lots is an established procurement-design object;
2. bidder entry, consortium formation, scope economies, coordination costs, and future procurement competition are established margins;
3. “more complementor entry” is not novel when it is only more bidder entry under a different name;
4. “unbundling improves future competition but sacrifices coordination” is not sufficient as a theorem;
5. an industrial-policy application does not create novelty without an irreducible strategic margin.

The old literature base was directionally correct: [Li, Sun, Yan, and Yu (2015)](https://doi.org/10.1016/j.jpubeco.2014.09.012), [Chen and Li (2018)](https://doi.org/10.1016/j.jpubeco.2018.02.004), [Buso (2019)](https://doi.org/10.1007/s00712-018-0642-0), [Giosa (2018)](https://doi.org/10.21552/epppl/2018/1/6), and [Chu and Wang (2015)](https://doi.org/10.1287/msom.2014.0517) already cover procurement scope, task interdependence, lotting, and effects on future competition.

## 3. What may have been prematurely removed

The old Stage 2 treated the question almost entirely as:

\\[
\text{lotting}
\rightarrow
\text{procurement bidder entry}.
\\]

That removed a distinct object that deserved an independent audit:

\\[
\text{procurement contract architecture}
\rightarrow
\text{persistent system architecture}
\rightarrow
\text{post-award complementor entry}
\rightarrow
\text{future market structure}.
\\]

The institutional audit supports this object in bounded complex-system settings:

- [EU Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014L0024) treats technical specifications and division into lots as separate design choices.
- [GOV.UK open-standards guidance](https://www.gov.uk/guidance/make-use-of-open-standards) links open standards and APIs to interoperability, upgradeability, and avoiding vendor lock-in.
- [OECD guidance on agile ICT procurement](https://www.oecd.org/en/publications/towards-agile-ict-procurement-in-the-slovak-republic_b0a5d50f-en/full-report/component-7.html) links modular contracting and up-front interoperability to reduced lock-in.
- [Acquisition.gov modular open-systems guidance](https://www.acquisition.gov/afars/appendix-aa-table-contents) connects open architecture and technical-data rights to lifecycle support competition.

The correction is important, but it establishes institutional plausibility—not theoretical novelty.

## 4. Literature frontier map

| Family | Decisive frontier | Implication |
|---|---|---|
| Procurement bundling/lotting | Li et al. (2015); Chen and Li (2018); Buso (2019); Giosa (2018) | Procurement scope and bidder entry are occupied |
| Procurement and future competition | Chu and Wang (2015); [Hanazono and Sato (2026)](https://doi.org/10.1016/j.econlet.2026.113129) | Current procurement affecting future competition is not new |
| Open technology and investment | [Hu, Hu, and Yang (2017)](https://doi.org/10.1287/msom.2016.0598) | Openness, supplier investment, and future competition already interact |
| Modularity and organization | [Argyres and Bigelow (2010)](https://doi.org/10.1287/orsc.1090.0493); [Arrieta, Fontana, and Brusoni (2023)](https://doi.org/10.1093/icc/dtac053) | Architecture already relates to vertical boundaries and entry |
| Compatibility and switching | [Farrell and Saloner (1985)](https://ideas.repec.org/a/rje/randje/v16y1985ispringp70-83.html); [Matutes and Regibeau (1988)](https://ideas.repec.org/a/rje/randje/v19y1988isummerp221-234.html); [Jeon, Menicucci, and Nasr (2023)](https://doi.org/10.1257/mic.20200309) | Strategic compatibility and future competition are mature |
| Platform/ecosystem openness | [Eisenmann (2008)](https://www.hbs.edu/ris/Publication%20Files/09-030.pdf); [Parker and Van Alstyne (2018)](https://doi.org/10.1287/mnsc.2017.2757); [Jovanovic, Sjödin, and Parida (2022)](https://doi.org/10.1016/j.technovation.2020.102218) | Complementor/developer entry and sponsor control are occupied |
| Recent architecture/competition | [Frenken and Romagnoli (2026)](https://doi.org/10.1093/icc/dtag047); [Ott et al. (2026)](https://doi.org/10.1093/joclec/nhag023); [Ekmekci, White, and Wu (2025)](https://doi.org/10.1287/mnsc.2023.02810) | Generic architecture–market-structure and interoperability–contestability claims face current prior art |

The full matrix is in [CLOSEST_PAPER_MATRIX.md](./CLOSEST_PAPER_MATRIX.md).

## 5. Procurement-stage entry versus post-procurement entry

| Dimension | Procurement-stage entry | Post-procurement complementor entry |
|---|---|---|
| Object | Tender participation, bidder count, consortium formation, SME access | Later modules, applications, maintenance, upgrades, replacement, support |
| Policy lever | Lotting, eligibility, award criteria, bundled scope | Interface/API, standards, portability, data rights, replacement and lifecycle terms |
| Timing | Before award and during auction | After deployment and during lifecycle competition |
| Persistence | Contract/award is the relevant state | Installed architecture and enforceable rights carry forward |
| Main private margin | Bid, form consortium, enter tender | Invest, enter complement market, license, multihome, or remain out |
| Main theory risk | Procurement bundling/lotting | Platform openness, compatibility, switching costs, vertical foreclosure, hold-up |
| Novelty requirement | Post-award state must alter private incentives | Effect must be more than a fixed entry-cost shift |

The re-audit accepts the second column as a different object. It does not accept the second column as automatically novel.

## 6. Reduction tournament

The complete tournament is in [REDUCTION_TESTS.md](./REDUCTION_TESTS.md). The decisive attacks were:

- **R1:** removing architecture reduces the question to procurement bundling/multi-sourcing;
- **R2:** open architecture lowering entrant fixed cost is a fatal parameter shift;
- **R3/R4:** a prime controlling access is vertical foreclosure or a platform sponsor choosing openness;
- **R5:** compatibility choice before downstream competition is standard;
- **R6:** persistence represented only by installed-base switching cost is lock-in theory;
- **R8/R9:** a private large buyer or a platform owner can reproduce the same result;
- **R11/R12/R13:** exogenous architecture, one known primitive, or terminology changes do not create a mechanism.

The strongest referee objection is:

> This is a standard openness/compatibility or vertical-foreclosure model with an auction placed in front of it. The auction selects the supplier; the supplier's post-award interface choice is the usual platform access choice.

The re-audit could not answer that objection without adding a new primitive after the fact.

## 7. Stage 2 decision

**CONDITIONAL SURVIVOR — NO CLEAN WHITE SPACE; ADVANCE ONLY TO AN ADVERSARIAL STAGE 3.**

The conditional status reflects a narrow search result: no single verified source was found with the entire public-contract-to-prime-architecture-to-independent-complementor chain. It is not a positive novelty finding. The individual components and near-complete combinations are already occupied.

## 8. Stage 3 variants and scores

Six mutually exclusive variants were tested in [STAGE3.md](./STAGE3.md):

| Variant | Mechanism | Total | Result |
|---|---|---:|---|
| M1 | Prime chooses open/closed architecture after award | 70 | KILL: platform/foreclosure |
| M2 | Costly interface investment | 66 | KILL: open technology/supplier investment |
| M3 | Lotting trades coordination against contestability | 68 | KILL: bundling plus compatibility |
| M4 | Procurement-created bottleneck ownership | 71 | KILL: vertical foreclosure/platform |
| M5 | Complementor relationship-specific investment and hold-up | 68 | KILL: hold-up/switching costs |
| M6 | Public buyer commits to interface/data rights | 76 | KILL: dynamic procurement plus standard openness/compatibility |

The required conditions were not met:

- no total reached 80;
- no mechanism-novelty score reached 21/25;
- no prior-art-survival score reached 16/20;
- every variant retained at least one fatal conceptual reduction.

## 9. Stage 4 minimal model

**Not executed.**

Stage 4 is a falsification test, not a mechanism-rescue device. Since no Stage 3 candidate survived the threshold and no-fatal-reduction gate, constructing a two-period buyer–prime–complementor model would only formalize an already identified standard model. There is therefore no verified parameter region, welfare theorem, or Stage 4 survivor to report.

## 10. Symbolic/computational verification

The scoring arithmetic was reproduced in [SCORING.py](./SCORING.py):

- M1 = 70
- M2 = 66
- M3 = 68
- M4 = 71
- M5 = 68
- M6 = 76

No equilibrium derivation was run because the Stage 4 gate did not open. This is deliberate: a closed-form model cannot convert a fatal structural reduction into novelty.

## 11. Final decision

The re-audit makes two statements simultaneously:

1. The old audit prematurely removed the post-award architecture distinction.
2. Restoring that distinction does not save the theme.

The correct final decision is therefore:

# **RE-AUDIT CONFIRMS OLD NO-GO**

No exact next research question is endorsed. The nearby leads in [PIVOT_CANDIDATES.md](./PIVOT_CANDIDATES.md) are only human-screening prompts and require fresh Stage 0 authorization.

**STOPPED — NO STAGE 4 SURVIVOR — NO STAGE 5 — NO STAGE 6 — NO PAPER WRITING**
