# Stage 1 — Source and Institutional Audit

## Scope

This audit tests whether the candidate primitive is institutionally real:

> A public buyer can choose contract architecture and technical/interface requirements that affect a system after award, including lifecycle interoperability, portability, support competition, and future replacement or complementor access.

The audit keeps two instruments separate:

1. **Lotting / scope architecture:** whether the procurement is divided into lots or awarded as one integrated contract.
2. **Technical and lifecycle architecture:** functional/performance specifications, interoperability, open standards, APIs/interfaces, data portability, technical-data rights, and support/replacement terms.

No source supports the shortcut “unbundling automatically creates interoperability.” The relevant institutional object, if any, is a joint contract-design problem in which lotting and technical/lifecycle terms can be chosen separately.

## Primary institutional evidence

### EU public procurement law

The EU Public Procurement Directive treats division into lots and technical specifications as separate procurement choices.

- Article 42 governs technical specifications. It permits specifications to refer to performance or functional requirements and, subject to safeguards, to standards and technical references.
- Article 46 separately addresses division of contracts into lots and requires contracting authorities to explain a decision not to subdivide above specified thresholds.

Source: [Directive 2014/24/EU, Articles 42 and 46](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014L0024).

Institutional implication: the law provides a clean basis for modeling lotting \\(L\\) and technical/interface requirements \\(I\\) as distinct policy dimensions. A model that makes \\(I=L\\) by definition would misstate the institutional design space.

### Open standards and interoperability

The UK Government Service Manual states that public bodies should make use of open standards, including standards for data, documents, and APIs, and links the practice to interoperability and avoiding vendor lock-in.

Source: [GOV.UK, Make use of open standards](https://www.gov.uk/guidance/make-use-of-open-standards).

The European Commission's Interoperable Europe guidance describes interoperability as reducing the cost of linking incompatible systems and treats open standards as a way to support competition and limit lock-in.

Source: [Interoperable Europe, Interoperability and vendor lock-in](https://interoperable-europe.ec.europa.eu/collection/ict-standards-procurement/interoperability-and-vendor-lock).

Institutional implication: open interface and portability clauses are plausible procurement instruments in ICT and digital-system procurement. They are not a universal feature of every public works or industrial contract.

### Modular contracting and lifecycle lock-in

The OECD's review of agile ICT procurement in the Slovak Republic explicitly links modular contracting to reduced vendor lock-in and says interoperability should be considered early when modular contracts are designed.

Source: [OECD, Towards Agile ICT Procurement in the Slovak Republic](https://www.oecd.org/en/publications/towards-agile-ict-procurement-in-the-slovak-republic_b0a5d50f-en/full-report/component-7.html).

The OECD's Digital Education Outlook distinguishes interoperability from openness: an interoperable system can use proprietary or open solutions, while open standards and data portability can reduce lock-in.

Source: [OECD, Interoperability: unifying and maximising data reuse](https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en/full-report/interoperability-unifying-and-maximising-data-reuse-within-digital-education-ecosystems_660f8da1.html).

Institutional implication: the candidate must not identify interoperability with openness. A rigorous model needs either (i) a specified interface/portability requirement that survives award, or (ii) an endogenous supplier choice over interface investment/architecture. A binary open/closed label with no contracting or lifecycle consequence is insufficient.

### Modular open systems and support competition

U.S. acquisition guidance for modular open systems architecture describes technical-data rights, modularity, and open interfaces as tools for avoiding vendor lock-in and fostering competition for sustainment and support over the life cycle.

Sources: [Acquisition.gov, Definitions and abbreviations](https://www.acquisition.gov/afars/chapter-5-definitions) and [Acquisition.gov, Appendix AA](https://www.acquisition.gov/afars/appendix-aa-table-contents).

Institutional implication: public procurement can affect not only the award-stage supplier but also later support, upgrade, replacement, and component markets. The source supports the persistence channel for digital/defense-like systems, but does not establish that the effect is present in all procurement settings.

## Primitive audit

| Required element | Institutional finding | Modeling status |
|---|---|---|
| Actual policy rule | Lotting and technical specifications are separate legal/design choices in EU procurement; open-standards guidance exists in digital procurement | Verified for relevant ICT/digital and modular-system settings |
| Applicant | Prime contractors, lot bidders, and suppliers apply/tender; future complementors need not be original bidders | Separate award-stage and post-award populations |
| Beneficiary | Public authority and downstream public users receive the procured system; future users may receive lower switching/upgrade costs | Model public buyer as purchaser and welfare-maximizer |
| Payment recipient | Awarded contractor(s) receive contract payment; later complementors receive lifecycle revenues only if they can enter | Procurement payment is not a generic innovation subsidy |
| Eligibility | Eligibility and technical compliance are set by tender documents; open standards/interface terms can be compliance conditions | Do not infer open access from lot eligibility alone |
| Selection mechanism | Lotting, technical specifications, functional requirements, and award criteria shape tender competition | Award stage is distinct from later market entry |
| Timing | Design/specification precedes tender and award; implementation and lifecycle support follow | At least two periods are institutionally plausible |
| Public/private roles | Public authority specifies/procures; private prime implements; independent suppliers may provide later modules/services | Three actor types are sufficient for a minimal model |
| Contractual structure | One integrated contract, multiple lots, framework/multi-vendor arrangement, interface/data rights, and support terms are possible | Lotting \\(L\\) and interface term \\(I\\) must remain separate |
| Cost incidence | Buyer bears contract price and may bear coordination/transaction cost; prime bears interface/modularity cost; future entrants bear entry/investment cost | Supports a welfare wedge, but its sign is not institutionally guaranteed |
| Downstream market relation | Lifecycle maintenance, upgrades, replacement, support, and complements can be procured after initial deployment | Post-award market must be explicitly defined |
| Entry/exit | Later suppliers may enter support/complement markets, but sources do not establish automatic entry rights | Entry is a theoretical strategic decision conditional on access |
| Matching | Procurement may select lots/suppliers; no universal public matching mechanism is established | Not needed in the minimal candidate |
| Exclusivity | Vendor lock-in and closed interfaces are recognized risks; exclusivity is not implied by all contracts | Must be modeled as an outcome or enforceable term, not assumed globally |
| Capacity | Implementation capacity and coordination constraints motivate integrated awards; no universal numeric capacity rule | Can enter as a single coordination-cost primitive if needed |
| Ownership/data/API | Technical-data rights, open interfaces, APIs, and portability are recognized in ICT/modular-system guidance | Must be contractually specified or chosen by the prime |
| Persistence | Lifecycle support, sustainment, switching, technical-data, and interface provisions can make architecture durable after award | Supported in relevant sectors, but requires an explicit persistence mechanism |
| Implementation constraint | Interoperability may require up-front design, standards compliance, documentation, or interface investment | Supports costly interface choice, not a free label |

## Persistence test

Persistence is not a consequence of lotting alone. It can arise from at least four institutionally grounded channels:

1. **Durable installed architecture:** the deployed system determines compatibility and replacement costs after the initial award.
2. **Contractual interface or portability terms:** technical specifications, data rights, API obligations, and open-system requirements survive into implementation and support.
3. **Lifecycle procurement:** maintenance, upgrades, and sustainment are later markets whose cost depends on the initial architecture.
4. **Switching and technical-data rights:** lack of documentation or access can make an initially selected supplier difficult to replace.

The audit therefore supports a *conditional* persistence primitive. It does not support a universal claim that every public procurement contract changes future market structure.

## Endogeneity test

The institutional sources imply three distinct cases:

- **Government-specified architecture:** the buyer directly mandates open standards, interfaces, portability, or modular requirements. This is a procurement/standards design problem, but may reduce to a standard compatibility or procurement-quality model.
- **Prime-chosen architecture:** the winner chooses an interface or modularity level after award. This can create a strategic architecture/foreclosure margin, but needs a reason why the procurement contract changes that incentive.
- **Contract-induced architecture:** lotting, award duration, data rights, lifecycle scope, evaluation, or support rights alter the prime's payoff from choosing open versus closed architecture. This is the only version with a plausible procurement-induced strategic feedback beyond an exogenous architecture dummy.

Stage 1 does not establish that the third case is theoretically novel. It establishes that it is institutionally coherent enough to test in Stage 2.

## Instrument-conflation finding

The old Cycle 1 formulation was vulnerable to conflating:

\\[
\text{unbundling} \equiv \text{interoperability}.
\\]

The sources reject that identity. Lotting governs procurement scope and bidder access; interoperability governs compatibility and lifecycle connection. They may be complementary, substitutes, or independent choices. The re-audit must keep them separate.

## Institutional limitation

The evidence is strongest for ICT, digital public infrastructure, defense/modular open systems, and other complex systems with lifecycle support. It does not justify claiming that a generic regional industrial-policy program or every public procurement contract creates a persistent complementor ecosystem.

## Stage 1 decision

**GO TO STAGE 2 — CONDITIONAL ON A SPECIFIED LIFECYCLE/PERSISTENCE CHANNEL.**

The primitive is real enough to audit theoretically, but only in a bounded class of complex-system procurement. Stage 2 must determine whether the resulting mechanism is distinct from existing procurement bundling, vertical foreclosure, platform openness, compatibility, switching-cost, modularity, and entry theory. If persistence is represented only by an exogenous open/closed dummy or if all post-award effects reduce to a fixed-entry-cost shift, the candidate must be killed.
