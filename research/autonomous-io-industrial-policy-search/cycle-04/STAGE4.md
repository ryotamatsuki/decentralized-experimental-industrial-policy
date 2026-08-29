# Cycle 04 — Stage 4 Minimal-Model Verification

## Frozen Stage-3 candidate

**M4.4 — Public-anchor learning and entry timing.**

The frozen claim was that a public pilot gives the selected supplier a
supplier-specific learning advantage and a verifiable signal; government
choice of early versus late release changes potential-entry timing and
therefore later competition.

Stage 4 tests exactly that mechanism. It adds no second instrument, no data
sharing, no regional dimension, no multiple suppliers, no platform, no
vertical-integration choice, and no new signal.

## Minimal model

There is one public buyer/government, one selected incumbent supplier, and one
potential entrant. The state is (s\in\{H,L\}), with
(Pr(H)=p\in(0,1)). The entrant's gross private profit is (v_H>v_L).
Entry costs (F>0).

The incumbent's binary learning action is (x\in\{0,1\}). If (x=1),
the entrant faces a supplier-specific barrier (b>0); the incumbent pays cost
(k) and receives learning rent (r). The public pilot provides revenue
(R). Entry reduces the incumbent's later rent by (Delta>0).

The government chooses one timing instrument:

- (d=E): release the verifiable pilot outcome before entry;
- (d=L): release it after entry, so the entrant has only the prior when it
  chooses.

The sequence is government timing choice, incumbent learning choice, signal
release according to (d), and entrant entry. The incumbent's payoff is
[
pi_I(d,x)=R+(r-k)x-Delta q_E^d(x),
]
where (q_E^d(x)) is the entrant's entry probability. The incumbent chooses
[
x^d\in\arg\max_{x\in\{0,1\}}\pi_I(d,x).
]
The government evaluates real social gains (G_H,G_L) from entry in the two
states, plus (Ax-K) from learning:
[
W_d(x)=
\begin{cases}
pG_H\mathbf 1\{v_H-F-bx\ge0\}
 +(1-p)G_L\mathbf 1\{v_L-F-bx\ge0\}+Ax-K,&d=E,\\
[pG_H+(1-p)G_L]\mathbf 1\{p(v_H-bx)+(1-p)(v_L-bx)-F\ge0\}
 +Ax-K,&d=L.
\end{cases}
]
This is a subgame-perfect backward-induction problem. The binary thresholds
are chosen only to make the existence and reduction tests transparent.

## Entrant equilibrium

Let
[
\bar v=pv_H+(1-p)v_L,\qquad \widetilde F=F+bx.
]
With early release,
[
q_E^E(x)=p\mathbf 1\{v_H\ge\widetilde F\}
 +(1-p)\mathbf 1\{v_L\ge\widetilde F\}.
]
With late release,
[
q_E^L(x)=\mathbf 1\{\bar v\ge\widetilde F\}.
]

Away from cutoff equalities, the four regions are:

| Effective cost | Early release | Late release |
|---|---:|---:|
| (widetilde F\le v_L) | (1) | (1) |
| (v_L<widetilde F\le\bar v) | (p) | (1) |
| (ar v<widetilde F\le v_H) | (p) | (0) |
| (widetilde F>v_H) | (0) | (0) |

Thus the effect exists on open parameter regions: for example,
(v_L<F+bx<\bar v) gives (q_E^E=p<1=q_E^L), while
(\bar v<F+bx<v_H) gives (q_E^E=p>0=q_E^L).
The incumbent's learning action changes the effective entry cost, but it does
not create a new strategic category of response.

## Required verification tests

### M1 — Existence

**Pass.** Release timing changes equilibrium entry on open inequalities, not
only at a cutoff. The Python verification script checks the four cutoff
regions over a finite grid and prints representative examples.

### M2 — Nontriviality

**Pass in the narrow sense.** Early versus late release changes conditional
entry and can alter the incumbent's entry deterrence motive:
[
x^d=1\quad\Longleftrightarrow\quad
r-k\ge\Delta[q_E^d(1)-q_E^d(0)].
]
But this is the standard information/entry threshold once the signal is
verifiable.

### M3 — Comparative-static robustness

**Pass.** Strict inequalities such as (v_L<F+bx<\bar v) define open regions.
The direction can reverse across the neighboring region
(\bar v<F+bx<v_H).

### M4 — Welfare wedge

**Pass, but not as a novel wedge.** The government can value entry
differently from the entrant through (G_H,G_L), so timing has a welfare
comparison. However, the sign is not pinned down by the public-anchor
learning story. With (p=.5,v_H=.9,v_L=.1,F=.4,bx=0):

- if (G_H=G_L=1), early welfare is (0.5), late welfare is (1);
- if (G_H=1,G_L=-.2), early welfare is (0.5), late welfare is (0.4).

The welfare ranking reverses under the same information structure.

### M5 — Minimality

**Fail for the claimed joint mechanism.** Set (b=0) and (x=0). The
learning advantage disappears, but early release still gives (q_E^E=.5)
and late release gives (q_E^L=1) at (p=.5,v_H=.9,v_L=.1,F=.4).
The entry-timing effect therefore does not require supplier-specific learning.

### M6 — Reduction to the closest standard model

**Fail.** After setting (b=0), the model is exactly a two-state public
disclosure problem followed by binary entry under an entry cost. The incumbent
learning action is payoff-irrelevant for entry in this reduction. A private
certifier/intermediary able to produce the same verifiable signal and choose
the same release date can reproduce the outcome because the model contains no
non-replicable public-input constraint.

### M7 — Edge cases

**Pass as a falsification check.**

- (p\in\{0,1\}): no informational uncertainty, so release timing has no
  effect.
- (v_H=v_L): no state-contingent entry, so timing has no effect.
- (b=0): learning disappears but the standard disclosure effect remains.
- no pilot/signal: the late/prior benchmark remains.
- (F+bx\le v_L) or (F+bx>v_H): both timing regimes give the same entry
  decision.

### M8 — Referee counterexample

**Fail for the intended theorem claim.** The welfare-ranking examples above
are simple sign reversals. They show that no robust policy ranking follows
without adding another primitive, such as a constrained public capacity,
non-replicable certification, or a richer continuation market. Each such
addition would violate the Stage-3 freeze and would be a rescue.

## Stage-4 decision

The narrow timing effect exists and is robust, but it is already generated by
standard public information disclosure plus entry. Supplier-specific learning
is not necessary; the welfare sign is not generated by the proposed public
anchor; and the closest standard model reproduces the mechanism.

**NO-GO — MINIMAL MODEL FAILS.**

No additional primitive is introduced to rescue M4.4. Cycle 04 is killed and
the controller must pivot to a nearby question.
