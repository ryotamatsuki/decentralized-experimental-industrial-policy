# Stage 3 — Candidate Mechanism Search

## 1. Executive mechanism-search verdict

- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MINIMAL MODEL`
- **Run status:** `MANDATORY STOP AFTER STAGE 3 — HUMAN APPROVAL REQUIRED`
- **Preferred candidate:** C4 — Competition to host a supplier’s scarce launch trial

Stage 3 generated eleven distinct mechanism candidates under the Stage 2 novelty kills. Three survive for possible minimal-model testing. C4 is preferred because it most directly creates a theoretically testable distinction between **support that changes whether an experiment occurs** and **support that merely changes where it occurs or transfers rent to the supplier**.

No formal payoff function, equilibrium, theorem or Stage 4 model has been constructed.

## 2. Frozen Stage 2 boundary

Stage 3 does not revive generic free riding, self-discovery, local-information federalism, decentralized experimentation, supplier commercialization, certification, or local subsidy competition as standalone contributions. The preferred mechanism must require their interaction.

A candidate must fail if it reduces to:

1. Callander–Harstad when supplier commercialization is removed;
2. Acemoglu–Bimpikis–Ozdaglar / Hausmann–Rodrik when jurisdictions/public sponsorship are removed;
3. ordinary PPI/procurement theory when host/follower geography is removed.

## 3. Candidate set

Eleven mechanisms were evaluated:

1. supplier co-financing / subsidy incidence;
2. local exclusivity versus disclosure;
3. local-fit uncertainty × reusable supplier learning;
4. competition to host a supplier’s scarce launch trial;
5. endogenous local re-validation / replication;
6. success-biased demonstration design / certification;
7. selective disclosure of trial outcomes;
8. local-retention conditionality versus diffusion;
9. sequential wait-versus-lead timing;
10. national co-financing × local skin in the game;
11. portfolio duplication / fashionable technologies.

Full mechanism descriptions are in `CANDIDATE_MECHANISMS.md`.

## 4. Pre-specified scoring

Weights: theoretical novelty 25, prior-art survival 20, mechanism clarity 15, welfare content 15, tractability 10, institutional relevance 10, empirical/journal bridge 5.

TOP results:

| Rank | Candidate | Score | Status |
|---|---|---:|---|
| 1 | C4 Competition to host supplier launch trial | 89 | **Preferred** |
| 1 | C6 Success-biased demonstration / certification | 89 | TOP 3 alternative |
| 3 | C3 Local-fit uncertainty × supplier learning | 85 | TOP 3 alternative |
| 4 | C1 Supplier co-financing / subsidy incidence | 81 | useful fallback/ingredient, not preferred |
| 5 | C11 Portfolio duplication | 79 | not TOP 3 |

The tie between C4 and C6 is resolved qualitatively, not mechanically by score.

## 5. TOP 3

### C4 — Competition to host a supplier’s scarce launch trial — PREFERRED

Core loop:

> The supplier’s downstream commercialization value determines whether one launch trial is worth conducting; local governments then compete to host that scarce trial because the host receives a local early-use/place benefit; the winning support may therefore affect only trial location/rent incidence rather than experiment occurrence, even though information later spills to non-host regions.

Why it survives Stage 2 provisionally:

- unlike pure federal experimentation, a private supplier internalizes downstream commercialization value and chooses whether/location of the trial;
- unlike private copying/self-discovery, decentralized public sponsors compete for the trial location;
- unlike ordinary PPI, non-host jurisdictions gain from an information-producing trial and local governments may bid for host-only value rather than simply procure their preferred innovation.

Potential contribution if Stage 4 mathematics supports it:

- a local subsidy can be **strictly unnecessary for experimentation** when supplier downstream rents already cover the extensive margin, yet jurisdictions may still pay to capture the host benefit;
- the same environment can exhibit **too little experimentation** when supplier + host benefits are insufficient but non-host information/adoption benefits make the trial socially worthwhile;
- policy therefore may partition into laissez-faire/private launch, productive support, wasteful hosting race, and higher-level coordination/co-financing regions.

Strongest referee objection:

> This is merely bidding for a mobile firm with an “experiment” label.

Stage 4 must defeat this by making the information-producing trial and supplier downstream commercialization jointly determine the **extensive margin**, so that removing either element changes the result.

### C6 — Success-biased demonstration design / certification

Core loop:

> Supplier downstream certification value and sponsor preference for visible success can make both parties choose an easy/high-success demonstration that produces less socially useful information than a harder test.

Potential contribution:

- success rate and learning value can diverge;
- stronger commercialization/certification incentives can lower experimentation informativeness;
- failure-tolerant evaluation or mandatory evidence standards may improve welfare.

Main threat:

PPI certification/signaling, voluntary disclosure, information design and political-credit literatures may already contain close mechanisms. It also needs more auxiliary assumptions than C4.

### C3 — Local-fit uncertainty × reusable supplier learning

Core loop:

> A local trial creates both public evidence about technology viability and supplier-owned adaptation know-how that improves later commercialization elsewhere.

Potential contribution:

- the supplier internalizes one component of experimentation value while other regions capture another;
- optimal public support may depend non-monotonically on transferability/appropriability of trial learning.

Main threat:

Detragiache-style adaptation externalities, private experimentation/copying and demonstration-learning literatures are close; a two-knowledge-component model risks becoming parameter-driven.

## 6. Why other candidates are not TOP 3

- **C1:** useful and tractable, but risks reducing to standard procurement risk sharing / supplier rents.
- **C2:** strong IPR/transparency prior-art threat.
- **C5:** potentially useful robustness, but local-fit heterogeneity can mechanically justify replication.
- **C7:** likely standard disclosure/signaling mechanism.
- **C8:** place-based retention/firm-location literature too close.
- **C9:** direct strategic/federal experimentation; rejected.
- **C10:** standard matching-grant/fiscal-federalism benchmark.
- **C11:** interesting “too many pilots, too little diversity” idea but Callander–Harstad already makes experiment diversity central and the portfolio structure adds complexity.

## 7. Targeted mini-search on TOP candidates

### C4

Targeted searches for local-government competition to host technology pilots/demonstration sites, launch-customer competition, supplier commercialization after public trials, and regional subsidy competition did not reveal an exact theory model matching the proposed joint structure. Adjacent literatures remain dense: local-authority PPI, public procurement as lead customer, local policy competition, public-procurement supplier market shaping, and demonstration policy.

**Classification remains:** `POTENTIALLY NOVEL / UNRESOLVED`; absence of an exact hit is not novelty proof.

### C6

Searches around demonstration success bias, certification, pilot design and supplier commercialization returned close PPI certification/signaling and demonstration-governance work but no exact retrieved model of an endogenous success-probability versus informativeness trade-off jointly preferred by sponsor and supplier.

**Classification:** `POTENTIALLY NOVEL / HIGH INFORMATION-DESIGN PRIOR-ART RISK`.

### C3

Searches reinforce existing multi-scale/local technology learning and adaptation-cost literatures. The distinction between public common evidence and supplier-private reusable know-how is plausible but more exposed to “two spillovers, two parameters” criticism.

**Classification:** `POTENTIALLY NOVEL / MEDIUM-HIGH PRIOR-ART AND MECHANICAL-RESULT RISK`.

## 8. Proposed narrowed research question if C4 is human-approved

> **How does a technology supplier’s downstream commercialization value affect decentralized governments’ incentives to subsidize and compete for the location of an information-producing launch trial, and when does local support create experimentation rather than merely relocate the trial or transfer rents?**

This proposed question does not replace the canonical Stage 0 question until the human hard gate approves C4.

## 9. Candidate propositions for Stage 4 kill-testing — C4 only

These are conjectures, not results:

1. **Non-additionality conjecture:** when the supplier’s expected downstream commercialization value is sufficient to induce the launch trial without local support, equilibrium local support may be positive solely because regions compete for the host benefit; support then creates no additional experimentation.
2. **Under-experimentation conjecture:** when supplier and host benefits together do not justify a trial but non-host informational/adoption benefits are sufficiently large, decentralized local support fails to induce a socially valuable experiment.
3. **Mislocation conjecture:** host bidding can place the trial in the region with the largest private/local host rent rather than the location that maximizes information quality or minimizes real trial cost.
4. **Higher-level intervention conjecture:** a national instrument targeted to the experimentation extensive margin can dominate unrestricted local hosting subsidies when cross-region information benefits are large.

Stage 4 must attempt to **kill**, not confirm, these conjectures.

## 10. Success/failure assessment

Stage 3 success criterion is met: at least one candidate has a clear loop, minimal implementable skeleton, welfare content and plausible proposition-level distance from the closest literature.

The project is not yet a paper. C4 could still fail Stage 4 because:

- the hosting race may reduce to a standard location-auction/subsidy model;
- local support may cancel as a transfer under welfare accounting;
- the under/over regions may be mechanically imposed by host/follower benefit parameters;
- the minimum equilibrium may fail to generate both extensive and location margins cleanly;
- a closer procurement/federal-experimentation paper may still be discovered.

## 11. Verdict and mandatory stop

- **Canonical verdict:** `GO`
- **Routing/status:** `GO TO MINIMAL MODEL`
- **Human recommendation:** approve C4 for Stage 4 before considering C6 or C3.
- **Mandatory status:** `STOPPED AFTER STAGE 3 — HUMAN APPROVAL REQUIRED BEFORE STAGE 4`

No Stage 4 work is authorized by this report.
