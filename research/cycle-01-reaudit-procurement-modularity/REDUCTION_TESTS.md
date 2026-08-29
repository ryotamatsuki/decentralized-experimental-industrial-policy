# Reduction Tests — Cycle 1 Re-Audit

## Decision rule

A “yes” to a fatal test kills the corresponding variant unless the post-procurement mechanism survives after the reduction. A label such as “public procurement” or “complementor” is not a primitive.

| Test | Reduction attack | Result for frozen candidate |
|---|---|---|
| R1 Procurement bundling | Replace the system by two tasks and let the buyer choose bundle versus separate lots; retain only bidder/consortium entry | **Fatal for the old question.** This reproduces the old Cycle 1 and the Li–Chen–Buso–Giosa family. A survivor must contain a post-award state and strategic response. |
| R2 Standard entry-cost model | Let open architecture imply only \(F_E^{open}<F_E^{closed}\) | **Fatal.** More complementor entry is then a parameter shift, not a mechanism. |
| R3 Vertical foreclosure | Interpret closed architecture as the prime denying rival access to an essential interface | **Strong kill threat.** This is a vertical foreclosure/raising-rivals'-costs model unless the procurement contract changes the prime's feasible payoff or ownership right in a way not present in the standard model. |
| R4 Platform openness | Replace public buyer and prime by a platform sponsor choosing access | **Strong kill threat.** Eisenmann and Parker–Van Alstyne reproduce the openness/rent-capture trade-off. Public procurement must alter the strategic timing or constraint, not merely the name of the platform owner. |
| R5 Compatibility/standards | Replace modular system by firms choosing compatibility before product-market competition | **Strong kill threat.** Farrell–Saloner, Katz–Shapiro, Matutes–Regibeau, Jeon–Menicucci–Nasr, and recent interoperability work already generate strategic compatibility and future competition. |
| R6 Switching costs/lock-in | Treat persistence only as an installed-base switching cost | **Strong kill threat.** The lifecycle result is a lock-in model unless the initial contract determines an endogenous right or investment that changes future access. |
| R7 Multi-sourcing | Treat separate lots as multiple sourcing or second sourcing, with no architecture choice | **Kill.** The effect is procurement diversification/second sourcing, not complementor entry through interfaces. |
| R8 Private-buyer replication | Replace the public buyer by a large private system buyer that values lifecycle cost and future competition | **Strong kill threat.** If equilibrium is unchanged, publicness is decorative. A public buyer can matter only through a noncontractible social/lifecycle objective, procurement constraint, or policy mandate that is explicit. |
| R9 Remove procurement stage | Start with a deployed system and let its sponsor choose openness | **Fatal to the procurement-induced claim.** If the same result remains, the paper is platform/compatibility theory. |
| R10 Remove modularity/interoperability | Delete interfaces and independent modules | **The post-award complementor result disappears.** This is necessary, but necessity is not novelty. |
| R11 Exogenous architecture | Set open/closed as a primitive dummy or impose it without a strategic choice | **Severe novelty downgrade; fatal for endogenous-architecture claims.** The model then has no procurement-to-architecture mechanism. |
| R12 One known primitive | Ask whether dynamic compatibility, foreclosure, switching costs, or supplier investment alone generates every proposition | **Fatal for the baseline.** At least one genuinely nonseparable interaction would be needed, and the current candidate has not demonstrated one. |
| R13 Relabeling | Rename platform sponsor as public buyer, developer as complementor, and access rule as procurement specification | **Fatal.** Names do not create industrial-policy economics. |

## Referee stress test

The strongest objection is:

> “This is a standard openness/compatibility or vertical-foreclosure model with an auction in front of it. The auction chooses the supplier, while the supplier's post-award interface choice is just the standard platform owner's access choice.”

The only possible response is an equilibrium condition in which the *contract architecture* changes the winner's private payoff from openness, while the public buyer's welfare objective values future contestability differently. That response is not enough by itself: the contract-induced payoff must not be a renamed switching cost, access fee, or investment incentive already in the matrix.

## Kill boundary

No variant may add data rights, ownership rights, lifecycle procurement, complementor investment, or a new policy instrument after seeing a failure. Each is tested below only when specified as that variant's single strategic margin. Combining two failed mechanisms would be rescue.
