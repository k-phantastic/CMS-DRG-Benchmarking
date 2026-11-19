# Medicare Hospital Price Benchmarking

![Status](https://img.shields.io/badge/status-in%20progress-D97706?style=flat-square)

Borne out of curiosity from a recent physical therapy trip I had and the exorbitant costs, this project benchmarks Medicare inpatient payments across U.S. hospitals, adjusts for the mix of cases each hospital treats, and uses statistical process control to flag hospitals whose payments fall outside expected limits. We look to explore how Medicare pays different hospitals for the same condition.

## Questions
1. How much does payment vary across hospitals for the same diagnosis-related group (DRG)?
2. Which hospitals charge the most relative to what Medicare actually pays?
3. Do rural hospitals get paid differently from urban hospitals for the same care?

## Data Sources
* [CMS Medicare Inpatient Hospitals by Provider and Service](https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service):

   **145,879 rows**, where each row is one hospital's average charges and payments for one DRG. The CMS data dictionary and methodology documents are in `data/`.

## Method
- **Cleaning pipeline:** a chain of pandas `.pipe()` steps that selects and renames columns, fixes data types, pads hospital and DRG codes, classifies hospitals as metro or non-metro from RUCA codes, and adds pricing metrics (markup and payment-to-charge ratio).

## Early results/EDA

## Progress
- Currently working on data ingestion and cleaning pipeline
- [x] Data ingestion and cleaning pipeline
- [ ] Price variation and case-mix index
- [ ] Markup and urban/rural analysis
- [ ] Funnel plot outlier detection
- [ ] Power BI dashboard

## Built with
`Python` `pandas` `NumPy` `Plotly` `Power BI`
