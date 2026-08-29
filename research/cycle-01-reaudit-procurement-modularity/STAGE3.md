# Stage 3 — Mechanism Search and Reduction Tournament

## Gate status

Stage 2 left a conditional route only. The six variants below are not six attempts to save the old question; they are six mutually exclusive tests of whether one contract-induced architecture margin escapes known models.

No new primitive is added after a variant fails. Scores were computed by the reproducible script [SCORING.py](./SCORING.py).

## Variant M1 — Post-award prime choice of open versus closed architecture

1. **ID:** M1.
2. **Research question:** Can the award contract change the prime's incentive to choose a persistent open interface rather than a closed one?
3. **Primitive:** \(a\in\{O,C\}\); the contract changes the prime's residual lifecycle payoff \(V_P(a;x)\).
4. **Players:** one public buyer, one winning prime, one potential complementor.
5. **Timing:** buyer chooses lotting/interface terms; prime is awarded the contract; prime chooses \(a\); complementor chooses entry; lifecycle competition occurs.
6. **Strategic action:** prime chooses architecture; complementor chooses entry.
7. **Externality/distortion:** the prime internalizes lost lifecycle rents from entry but not buyer/user contestability value.
8. **Government instrument:** lotting and enforceable interface/portability requirements.
9. **Equilibrium intuition:** the prime closes when the residual lifecycle rent from exclusion exceeds the private value of openness; it opens when the contract removes the exclusion rent or rewards compatibility.
10. **Welfare intuition:** the buyer may prefer openness when future replacement/innovation value exceeds coordination savings.
11. **Closest model:** platform openness, vertical foreclosure, and dynamic procurement.
12. **Reduction threat:** if \(x\) only changes an entrant fixed cost or access fee, R2; if the prime is simply a platform sponsor, R4; if closure denies access to an essential facility, R3/R5.
13. **Generality:** applies to digital infrastructure, defense systems, industrial equipment, and other lifecycle systems.
14. **Minimum assumptions:** durable installed base, prime control of a technically meaningful interface, one later entrant, and a lifecycle payoff.
15. **Candidate proposition:** a contract can induce openness only when it changes the prime's residual payoff, but the comparative static is already a standard openness/foreclosure result.
16. **Kill condition:** replace the public buyer by a platform owner or large private buyer and retain the same payoff; no procurement-specific result remains.

**Status:** KILL — structural containment under R3/R4/R5/R11/R12.

## Variant M2 — Costly interface investment

1. **ID:** M2.
2. **Research question:** Does procurement change a prime's costly investment in interface quality, thereby inducing complementor investment and later competition?
3. **Primitive:** \(m\ge 0\), with cost \(c(m)\); higher \(m\) reduces complementor access cost and may improve coordination.
4. **Players:** public buyer, prime, one complementor.
5. **Timing:** buyer specifies contract; prime chooses \(m\); complementor observes access and invests/enters; lifecycle market follows.
6. **Strategic action:** prime chooses interface investment; complementor chooses relationship-specific investment and entry.
7. **Externality/distortion:** the prime bears the cost of making future access contestable but captures only part of the buyer's future surplus.
8. **Government instrument:** contractible interface investment requirement or lifecycle payment.
9. **Equilibrium intuition:** the prime underinvests when openness lowers future rents; complementor investment can reinforce the value of openness.
10. **Welfare intuition:** the buyer may mandate \(m\) when future support and innovation benefits exceed implementation cost.
11. **Closest model:** [Hu, Hu, and Yang (2017)](https://doi.org/10.1287/msom.2016.0598), open technology, supplier investment, and competition.
12. **Reduction threat:** if \(m\) only lowers \(F_E\), R2; if it is technology sharing by a private manufacturer, R4/R5/R12.
13. **Generality:** potentially broad, but the public-procurement setting supplies no distinct payoff unless rights and lifecycle obligations matter.
14. **Minimum assumptions:** costly interface investment, one complementor, and residual post-award rents.
15. **Candidate proposition:** openness can increase complementor investment while intensifying future competition; this is already the core trade-off in the closest model.
16. **Kill condition:** if the buyer is removed and a private platform/manufacturer makes the same investment choice, the procurement claim disappears.

**Status:** KILL — Hu et al. (2017) and platform/compatibility containment; R2/R4/R5/R12 fatal.

## Variant M3 — Lotting as a coordination-versus-contestability choice

1. **ID:** M3.
2. **Research question:** Can the buyer choose integrated versus separate lots while separately choosing interface terms, trading current coordination against future complementor contestability?
3. **Primitive:** \(L\in\{I,S\}\) (integrated/separate scope) and an interface term \(q\); \(L\) affects coordination cost and the prime's control over the interface.
4. **Players:** public buyer, prime/lot suppliers, one later complementor.
5. **Timing:** buyer selects \((L,q)\); procurement award occurs; implemented architecture persists; complementor enters; lifecycle market follows.
6. **Strategic action:** buyer chooses \(L,q\); prime chooses compliance/architecture if discretion remains; complementor chooses entry.
7. **Externality/distortion:** integrated scope saves coordination cost but can leave one supplier with an exclusionary bottleneck; separate lots can preserve future supplier access.
8. **Government instrument:** lotting plus technical/interface specifications.
9. **Equilibrium intuition:** separate lots are attractive only if they change future access or control, not merely the number of bidders.
10. **Welfare intuition:** the buyer may sacrifice scope economies for future replacement and innovation.
11. **Closest model:** procurement bundling/lotting plus multi-sourcing, dynamic procurement, and platform openness.
12. **Reduction threat:** remove \(q\) and it is R1/R7; make \(q\) exogenous and it is R2/R5; let the winning prime be a platform owner and it is R4.
13. **Generality:** broad only as a contract-design framing; the substantive mechanism is narrow.
14. **Minimum assumptions:** separate lotting and interface rights, persistent lifecycle use, and one later entry opportunity.
15. **Candidate proposition:** unbundling is welfare-improving only when it changes future control/entry, not when it simply creates more procurement bidders.
16. **Kill condition:** if the lotting variable affects only procurement-stage participation or diversification, the post-award mechanism vanishes.

**Status:** KILL — the surviving part is the old bundling result plus an exogenous compatibility condition; R1/R2/R5/R7/R11 fatal.

## Variant M4 — Procurement-created bottleneck ownership

1. **ID:** M4.
2. **Research question:** Does awarding a bottleneck module to a prime allow it to foreclose later complementors, with lotting determining bottleneck ownership?
3. **Primitive:** the winner controls an indispensable interface or bottleneck module and chooses access.
4. **Players:** public buyer, bottleneck incumbent, potential complementor.
5. **Timing:** buyer assigns scope/lot; incumbent implements bottleneck; complementor requests access and enters; incumbent and complementor compete.
6. **Strategic action:** incumbent chooses access/exclusivity; complementor chooses entry.
7. **Externality/distortion:** incumbent values exclusionary lifecycle rents; buyer values future supply and lower replacement cost.
8. **Government instrument:** ownership/data-right/interface clauses and lot assignment.
9. **Equilibrium intuition:** incumbent closes or raises access cost when the downstream margin is profitable.
10. **Welfare intuition:** public access rights can prevent lifecycle foreclosure.
11. **Closest model:** vertical foreclosure/raising rivals' costs, essential facilities, and platform access.
12. **Reduction threat:** the bottleneck is a direct foreclosure primitive; installed-base persistence is a switching-cost version.
13. **Generality:** relevant to defense, software, and complex equipment, but not a new theory without a special procurement constraint.
14. **Minimum assumptions:** indispensable interface, incumbent control, one entrant, and downstream profits.
15. **Candidate proposition:** awarding a bottleneck without access rights can create a durable monopoly in the complement market.
16. **Kill condition:** reproduce the same game with a private vertically integrated buyer or platform owner.

**Status:** KILL — direct vertical foreclosure/platform model; R3/R4/R6/R8/R12 fatal.

## Variant M5 — Complementor relationship-specific investment and hold-up

1. **ID:** M5.
2. **Research question:** Does an expected public procurement architecture change complementor investment before entry, creating a welfare case for portability or open access?
3. **Primitive:** complementor chooses relationship-specific investment \(k\) conditional on expected access; the prime can later deny or exploit access.
4. **Players:** public buyer, prime, potential complementor.
5. **Timing:** buyer commits to contract rights; prime implements; complementor invests and enters; access/rents are realized.
6. **Strategic action:** complementor invests/enters; prime chooses access or hold-up if discretion remains.
7. **Externality/distortion:** complementor investment creates future variety/competition not fully appropriated by the buyer; prime may hold up the entrant.
8. **Government instrument:** portability, data/interface rights, certification, or a non-discrimination clause.
9. **Equilibrium intuition:** credible access increases \(k\) and entry; weak rights deter sunk investment.
10. **Welfare intuition:** access rights can solve underinvestment but can reduce the prime's incentive to build the system.
11. **Closest model:** switching costs, hold-up, vertical contracting, and platform complementor investment.
12. **Reduction threat:** if contract rights only reduce switching costs, R6; if a platform sponsor grants access, R4; if procurement is only a commitment date, dynamic contracting contains it.
13. **Generality:** relevant to lifecycle suppliers, but not specific to public procurement.
14. **Minimum assumptions:** relationship-specific complementor investment, enforceable access term, and post-award hold-up.
15. **Candidate proposition:** stronger portability can increase entry investment but may reduce prime investment; the sign depends on standard hold-up parameters.
16. **Kill condition:** if the same investment and access game survives without the procurement stage, it is not procurement-induced.

**Status:** KILL — standard hold-up/switching-cost/platform access; R4/R6/R12 fatal.

## Variant M6 — Architecture commitment by the public buyer

1. **ID:** M6.
2. **Research question:** Can the buyer commit at award to future interface/data rights, changing the prime's lifecycle rent and the complementor's entry decision?
3. **Primitive:** a committed contract state \(x\) determines future access rights; the prime chooses its implementation within \(x\); the complementor responds.
4. **Players:** public buyer, prime, one complementor.
5. **Timing:** buyer commits to \(x\); procurement award; prime chooses architecture/compliance; complementor enters; future market competition occurs.
6. **Strategic action:** buyer chooses commitment; prime chooses residual architecture; complementor chooses entry.
7. **Externality/distortion:** the buyer values contestability and lifecycle innovation; the prime values exclusivity and may discount future public benefits.
8. **Government instrument:** contractually enforceable interface, technical-data, portability, and replacement rights.
9. **Equilibrium intuition:** commitment can eliminate the prime's ability to close access, but this is a standard commitment/open-access effect unless the contract changes the prime's feasible action set in a novel way.
10. **Welfare intuition:** early commitment can dominate ex-post regulation when the installed system creates lock-in.
11. **Closest model:** [Chu and Wang (2015)](https://doi.org/10.1287/msom.2014.0517), dynamic procurement and future competition; [Hanazono and Sato (2026)](https://doi.org/10.1016/j.econlet.2026.113129), compatibility and investment incentives in dynamic procurement; platform/compatibility commitment.
12. **Reduction threat:** a commitment date is not a new mechanism; if \(x\) is just an access rule, R4/R5; if it only changes entry cost, R2; if the buyer is private, R8.
13. **Generality:** institutional relevance is strongest for complex public systems with lifecycle support.
14. **Minimum assumptions:** two periods, durable contract rights, one prime, one complementor, and a future market.
15. **Candidate proposition:** the public buyer may choose stronger commitment than a private buyer when it values future contestability more than the prime does.
16. **Kill condition:** derive the same result from a standard dynamic procurement or platform openness game by renaming the buyer and access rule.

**Status:** KILL — highest-scoring but still below threshold and fatally reducible to dynamic procurement plus platform/compatibility commitment.

## Stage-3 score table

| Variant | Mechanism novelty /25 | Prior-art survival /20 | Strategic distinctiveness /15 | Welfare /10 | Industrial policy /10 | Theorem /7 | Minimality /5 | Tractability /5 | Generality /3 | Total | Fatal reduction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| M1 | 16 | 10 | 11 | 8 | 9 | 5 | 4 | 4 | 3 | **70** | Yes: R3/R4/R5/R11/R12 |
| M2 | 15 | 10 | 10 | 8 | 8 | 5 | 3 | 4 | 3 | **66** | Yes: R2/R4/R5/R12 |
| M3 | 15 | 9 | 11 | 9 | 9 | 5 | 3 | 4 | 3 | **68** | Yes: R1/R2/R5/R7/R11 |
| M4 | 17 | 11 | 12 | 8 | 9 | 5 | 3 | 3 | 3 | **71** | Yes: R3/R4/R6/R8/R12 |
| M5 | 16 | 11 | 11 | 8 | 8 | 5 | 3 | 3 | 3 | **68** | Yes: R4/R6/R12 |
| M6 | 18 | 12 | 12 | 9 | 10 | 6 | 3 | 3 | 3 | **76** | Yes: R2/R4/R5/R8/R12 |

## Stage-3 decision

No variant reaches the required threshold of total \(\ge 80\), mechanism novelty \(\ge 21\), and prior-art survival \(\ge 16\). More importantly, every variant has a fatal reduction:

- M1 and M4 are vertical foreclosure/platform-access models.
- M2 and M5 are openness/supplier-investment or hold-up models.
- M3 is procurement bundling plus an exogenous compatibility condition.
- M6 is dynamic procurement commitment plus a standard openness/compatibility rule.

**NO-GO — NO STAGE-4 CANDIDATE.**

Stage 4 is not run. A minimal model cannot be used to rescue a candidate whose only surviving margins are already standard-model margins.
