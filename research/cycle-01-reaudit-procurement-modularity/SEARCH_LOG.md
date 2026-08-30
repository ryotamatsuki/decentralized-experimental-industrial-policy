# Search Log — Cycle 1 Re-Audit

Date of audit: 2026-08-29

## Search protocol

The re-audit searches both canonical and recent literature through August 2026. Priority was given to publisher pages, official repositories, RePEc metadata pages, government guidance, EU legal text, OECD reports, and primary working-paper or journal pages.

The audit separates:

- procurement-stage bidder/consortium entry;
- post-procurement complementor, support, replacement, and upgrade entry;
- architecture/interoperability as a technical or governance choice;
- future competition and market-structure effects.

## Institutional searches

| Query/theme | Main sources checked | Initial finding |
|---|---|---|
| Division into lots / technical specifications | [EU Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014L0024) | Lotting (Article 46) and technical specifications (Article 42) are distinct instruments |
| Open standards / APIs / lock-in | [GOV.UK open standards](https://www.gov.uk/guidance/make-use-of-open-standards); [Interoperable Europe](https://interoperable-europe.ec.europa.eu/collection/ict-standards-procurement/interoperability-and-vendor-lock) | Open standards and interoperability are used to support connection and reduce vendor lock-in |
| Modular contracting | [OECD Slovak Republic ICT procurement](https://www.oecd.org/en/publications/towards-agile-ict-procurement-in-the-slovak-republic_b0a5d50f-en/full-report/component-7.html) | Modular contracting and up-front interoperability are linked institutionally |
| Openness vs interoperability | [OECD Digital Education Outlook](https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en/full-report/interoperability-unifying-and-maximising-data-reuse-within-digital-education-ecosystems_660f8da1.html) | They are not synonymous; proprietary systems can interoperate |
| Lifecycle support / technical data / open systems | [Acquisition.gov definitions](https://www.acquisition.gov/afars/chapter-5-definitions); [Appendix AA](https://www.acquisition.gov/afars/appendix-aa-table-contents) | Open-system architecture and technical-data rights are used to preserve lifecycle support competition |

## Theory searches

| Family | Queries | Sources selected for Stage 2 |
|---|---|---|
| Procurement bundling and lotting | procurement bundling lotting bidders consortia; division public contracts lots; bundled procurement sequential tasks | Li, Sun, Yan & Yu (2015); Chen & Li (2018); Buso (2019); Giosa (2018); Chiappinelli, Giuffrida & Spagnolo (2025) |
| Procurement and future competition | procurement technology acquisition future competition; dynamic procurement follow-on competition; public procurement market structure | Chu & Wang (2015); Wan (2014); OECD innovation procurement (2024); OECD ICT procurement (2024) |
| Modularity and industry structure | modularity vertical disintegration entry industry organization; product architecture market structure | Argyres & Bigelow (2010); Arrieta, Fontana & Brusoni (2023); Thun (2022); Baldwin (2017); Frenken et al. (2026) |
| Interoperability and competition | compatibility interoperability entry switching standards competition | Farrell & Saloner (1985); Katz & Shapiro (1985); Matutes & Regibeau (1988); Economides (1989); Jeon, Menicucci & Nasr (2023); Ekmekci, White & Wu (2025); Riley (2020); Ott (2026) |
| Platforms and complementors | platform openness complementor entry architecture governance; API openness ecosystem | Eisenmann (2008); Chen, Yi, Li & Tong (2022); Jovanovic, Sjödin & Parida (2022); Jacobides et al. (2024); Fang (2021); Chen et al. (2026) |
| Public procurement and standards/interoperability | public procurement interoperability competition; modular public procurement; vendor lock-in open standards; procurement APIs competition | EU Directive 2014/24/EU; GOV.UK; OECD; Interoperable Europe; Acquisition.gov |

## Search limitations

Some publisher pages expose abstracts and metadata while withholding full text. Claims in the Stage 2 matrix are limited to the mechanism/result visible from the source or publisher metadata. Bibliographic metadata will be added only where author/year/title/journal/volume/issue/pages or article number/DOI can be verified from a publisher or authoritative bibliographic page.


## Stage 2 deep-literature search additions

Searches completed on 2026-08-29:

- `procurement bundling future competition technology acquisition`
- `compatibility investment incentives dynamic procurement`
- `open technology supplier investment future competition`
- `product modularity vertical deintegration entry industry structure`
- `compatibility switching costs data portability competition`
- `platform openness complementor entry architecture governance`
- `public procurement modular open systems interoperability vendor lock-in`
- `market structure product architecture 2026`
- `standardization interoperability entry contestability 2026`

Key additions:

- Chu and Wang (2015), *Bundled Procurement for Technology Acquisition and Future Competition*, explicitly connects current procurement scope to future market competition.
- Hu, Hu, and Yang (2017), *Open or Closed? Technology Sharing, Supplier Investment, and Competition*, directly models openness, supplier investment, and future competition; the publisher keywords include procurement.
- Hanazono and Sato (2026), *Compatibility and Investment Incentives in Dynamic Procurement*, is a near-exact 2026 threat linking compatibility, investment, and dynamic procurement. The issue record is Economics Letters 268, article 113129, DOI 10.1016/j.econlet.2026.113129.
- Jeon, Menicucci, and Nasr (2023) models dynamic compatibility choices, switching costs, and data portability.
- Parker and Van Alstyne (2018) models platform openness, third-party developer investment, and control.
- Argyres and Bigelow (2010), Arrieta et al. (2023), and Frenken and Romagnoli (2026) connect product architecture/modularity to vertical organization, entry, or market structure.
- Ekmekci, White, and Wu (2025) and Ott, Roter, and Krämer (2026) provide recent competition/interoperability and standardization/contestability evidence.

## Stage 2/3 result

The search did not verify an exact paper containing the full public-procurement-to-prime-architecture-to-independent-complementor-entry chain. It did verify enough structural coverage to make the white space narrow. Stage 2 was classified as a conditional survivor only for an adversarial Stage 3 reduction tournament.

Stage 3 tested six mutually exclusive minimal variants. Python scoring produced totals M1=70, M2=66, M3=68, M4=71, M5=68, M6=76. Every variant failed the no-fatal-reduction requirement; no Stage 4 model was authorized.
