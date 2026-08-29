# Final Report — Autonomous IO–Industrial Policy Search

Date: 2026-08-29
Scope: Industrial Policy × Industrial Organization
Controller limit: five cycles
Allowed stages: Stage 0 through Stage 4 only

## Final result

**NO SURVIVING THEME AFTER 5 CYCLES**

The search produced no candidate satisfying the required combination of a
distinct strategic mechanism, a clear welfare wedge, survival against closest
prior art, and a plausible minimal theorem.

## Tested questions

| Cycle | Question | Highest stage | Result |
|---:|---|---|---|
| 1 | Does public-procurement lotting create a new complementor-entry mechanism? | Stage 2 | NO-GO: procurement bundling and scope choice contain the mechanism |
| 2 | Does public deployment-data access create a distinct downstream competition mechanism? | Stage 2 | NO-GO: exact/high-overlap learning-by-deploying and data-competition theory |
| 3 | Does eligibility for direct performance versus external capacity create a new vertical-boundary mechanism? | Stage 2 | NO-GO: entry, subcontracting, and vertical-organization theory contain it |
| 4 | Does a public pilot's supplier-specific learning advantage make early/late signal release change later entry in a novel way? | Stage 4 | NO-GO: the effect exists, but remains after learning is removed and reduces to standard disclosure plus entry |
| 5 | Does an advance public purchase commitment induce capacity investment while deterring later entry after re-tendering? | Stage 2 | NO-GO: dynamic procurement, commitment, investment, and supplier competition already contain it |

## Cycle 4 falsification result

Cycle 4 was the only candidate to reach a formal model. The frozen model had
one government/public buyer, one incumbent, one entrant, a binary state, a
supplier-specific learning barrier b x, and an early versus late public
release decision.

With v̄ = p v_H + (1-p) v_L and effective entry cost F + b x:

- if v_L < F + b x < v̄, early release gives entry probability p and late
  release gives entry probability 1;
- if v̄ < F + b x < v_H, early release gives p and late release gives 0.

These effects hold on open parameter regions. But setting b = 0 removes the
supplier-specific learning advantage while leaving the timing effect intact.
The reduced model is exactly public information disclosure followed by a
binary entry decision. Welfare rankings also reverse across simple
state-surplus configurations. The Stage-4 verdict was therefore
NO-GO — MINIMAL MODEL FAILS.

The Python verification is stored in
cycle-04/VERIFICATION.py, and the complete M1–M8 audit is in
cycle-04/STAGE4.md.

## Cross-cycle lessons

1. Public procurement mechanisms repeatedly collapsed into established
   contract-design, entry, subcontracting, investment, and dynamic-procurement
   families.
2. Adding a public label—pilot, innovation procurement, regional programme, or
   demand pull—did not create a new strategic margin.
3. A market-structure consequence is not sufficient for novelty if the same
   consequence follows from a standard buyer commitment, entry, information,
   or vertical-contracting primitive.
4. The most promising-looking Cycle 4 mechanism failed the minimality test:
   the claimed public-anchor learning component was not necessary for the
   entry-timing effect.
5. The main surviving methodological lesson is negative: the policy
   instruments most naturally suggested by the motivating institutions are
   already tightly connected to mature IO theory and require unusually strong
   evidence of a non-replicable public role.

## Nearby families not tested after the hard stop

These are frontier-map items, not surviving candidates and not an authorization
for a sixth cycle:

- non-replicable public implementation assets with explicit access and
  ownership rights, kept separate from the killed coalition-composition grant
  and from generic learning;
- interoperability or portability rules tied to an enforceable public
  procurement contract and complementor entry;
- public-platform governance where public capacity is genuinely
  non-replicable rather than a relabeled subsidy or data-sharing rule;
- procurement renewal/renegotiation with a genuinely non-contractible service
  dimension and endogenous entry, subject to the high dynamic-procurement
  prior-art risk;
- acquisition, exit, or merger restrictions after public demand creation;
- demand aggregation with endogenous market formation beyond ordinary lotting,
  subject to a fresh bundling audit.

The frozen C5 and C7 backups do not receive priority. None of these nearby
families was promoted or modeled in this run.

## Stop rule

The fifth cycle ended at Stage 2 with a NO-GO. The maximum cycle budget is
zero, so no sixth cycle was started. No Stage 5, Stage 6, manuscript,
introduction, abstract, empirical section, or policy-recommendations section
was produced.
