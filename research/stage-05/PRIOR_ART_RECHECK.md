# Stage 5 Prior-Art Re-Check

Search date: 2026-08-28.

Purpose: test the **actual Stage 5 q_i mechanism**, not the intended application label, against the literatures triggered by the one authorized modification.

## 1. Jehiel, Moldovanu & Stacchetti (1999) — auctions with identity-dependent externalities

Philippe Jehiel, Benny Moldovanu, and Ennio Stacchetti, “Multidimensional Mechanism Design for Auctions with Externalities,” *Journal of Economic Theory* 85(2), 1999, 258–293. DOI: `10.1006/jeth.1998.2501`.

The paper's general auction environment explicitly allows a bidder who loses to care about **which rival wins**. A bidder's type specifies the payoff for each possible allocation outcome, including the seller retaining the object. It studies incentive-compatible mechanisms and scalar-bid auctions under these externalities.

Stage 5 mapping:

- object / allocation: the scarce launch-trial host status;
- bidder: local jurisdiction;
- seller/object owner: technology supplier choosing whether/where to launch;
- own-win payoff before transfer: `q_i E + H`;
- lose-to-j payoff: `q_j E`;
- no-allocation payoff: zero;
- supplier participation gap `F`: an allocation/reserve condition.

Therefore the new Stage 5 fact that `q_i` changes a government's bid because losing to a high-q host is more valuable is **not a new strategic class**. It is a particularly transparent application of identity-dependent allocation externalities.

Classification: `STRUCTURALLY VERY CLOSE / GENERAL THEORY CONTAINS THE CORE STRATEGIC LOGIC`.

Sources:
- https://doi.org/10.1006/jeth.1998.2501
- https://ideas.repec.org/a/eee/jetheo/v85y1999i2p258-293.html

## 2. Jehiel & Moldovanu (2000) — auctions with downstream interaction

Philippe Jehiel and Benny Moldovanu, “Auctions with Downstream Interaction among Buyers,” *RAND Journal of Economics* 31(4), 2000, 768–791. DOI: `10.2307/2696358`.

The auction outcome changes payoffs through later/downstream interactions; the paper derives bidding equilibria and studies reserve prices, entry fees and welfare.

Stage 5 implication: interpreting the launch site as changing downstream information/adoption values does not by itself distinguish the model from auction-with-externalities theory. The supplier's option not to launch and the participation gap likewise do not create an obviously separate mechanism.

Classification: `STRUCTURALLY VERY CLOSE`.

Source: https://doi.org/10.2307/2696358

## 3. Slattery (2025) and Mast (2020) — local subsidy competition

Cailin Slattery, “Bidding for Firms: Subsidy Competition in the United States,” *Journal of Political Economy* 133(8), 2025, 2563–2614. DOI: `10.1086/735509`.

Slattery models state/local governments bidding with subsidies for mobile firms using an auction framework. Heterogeneity in governments' valuations and location substitutability determines rent allocation; competition can transfer rents to firms.

Evan Mast, “Race to the Bottom? Local Tax Break Competition and Business Location,” *AEJ: Applied Economics* 12(1), 2020, 288–317. DOI: `10.1257/app.20170511`.

Stage 5 implication: the fiscal-rent/overpayment side of C4 remains occupied. `q_i` changes valuations, but heterogeneous local valuations in a location auction are already central to this literature.

Classification: `STRUCTURALLY VERY CLOSE` for the bidding/rent side; `COMPONENT OVERLAP` for information production.

## 4. Callander & Harstad (2015) — heterogeneous experimentation and informational spillovers

Steven Callander and Bård Harstad, “Experimentation in Federal Systems,” *Quarterly Journal of Economics* 130(2), 2015, 951–1002. DOI: `10.1093/qje/qjv008`.

Their heterogeneous districts choose whether and what to experiment with; informational spillovers create strategic distortions in experiment choices and policy divergence.

Stage 5 implication: a decentralized-versus-social wedge caused by jurisdictions internalizing only part of the information value of heterogeneous experiments is not new by itself. C4's distinctive object is private-supplier host allocation, but the information-spillover comparative statics cannot carry the contribution.

Classification: `COMPONENT OVERLAP / STRONG MECHANISM THREAT`.

## 5. Gechter et al. — experimental-site selection for external validity

Michael Gechter et al., “Selecting Experimental Sites for External Validity,” working paper/arXiv:2405.13241, 2024–2026 circulation.

The paper takes a decision-theoretic approach to choosing experimental sites for external validity and shows potentially large efficiency losses from nonoptimal site selection.

Stage 5 implication: the proposition “experimental location affects generalizable information and the planner should choose a high-information site” is occupied independently of subsidy competition. `q_i` is therefore a credible primitive, but not a novelty claim.

Classification: `COMPONENT OVERLAP / DIRECT SITE-SELECTION THREAT`.

Source: https://arxiv.org/abs/2405.13241

## 6. Volunteer-dilemma literature

David Myatt and Chris Wallace, “An Evolutionary Analysis of the Volunteer's Dilemma,” *Games and Economic Behavior* 62(1), 2008, 67–76. DOI: `10.1016/j.geb.2007.03.005`.

Toshiji Kawagoe, Hirokazu Takizawa, and Tetsuo Yamamori, “Asymmetric Volunteer's Dilemma Game: Theory and Experiment,” *Games and Economic Behavior* 142, 2023, 955–977. DOI: `10.1016/j.geb.2023.10.009`.

The literature already emphasizes multiple pure volunteer equilibria, asymmetric provision incentives and equilibrium-selection problems; an inefficient or counterintuitive volunteer need not be a new result.

Stage 5 implication: the low-q volunteer equilibrium and the mixed-equilibrium host bias are mathematically valid but cannot credibly serve as the main novelty without a distinct experiment-specific feedback beyond asymmetric public-good provision.

Classification: `STRUCTURALLY CLOSE TO THE HIGH-RESERVE/VOLUNTEER BLOCK`.

## 7. What the search did and did not establish

No single retrieved paper was found that uses the exact institutional labels:

`local governments + private technology supplier + one launch trial + q_i information quality + host subsidy`.

That absence is not novelty evidence.

At the level of strategic structure, the Stage 5 model decomposes into already-established families:

1. low-reserve allocation: **auction/location competition with identity-dependent externalities**;
2. high-reserve provision: **asymmetric volunteer/public-good problem**;
3. experiment-location welfare: **heterogeneous experimentation / external-validity site selection**;
4. fiscal overpayment: **local subsidy competition**.

The one authorized change therefore solves the Stage 4 algebraic separability problem but does not generate a sufficiently distinct model/proposition-level mechanism.

## 8. Prior-art verdict

`NO-GO SUPPORTING FINDING`.

The strongest reason is not merely that each component is known separately. The **new q_i strategic feedback itself**—a loser caring about who hosts, which changes willingness to bid—is the canonical externality-auction structure. The remaining mislocation result is multiplicity/mixed provision from an asymmetric volunteer block rather than a new unique experiment-location distortion.

A second substantive modification would be required to produce a different strategic interaction. Stage 5 governance forbids that rescue.
