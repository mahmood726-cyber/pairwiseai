# E156 Protocol — `Pairwiseai`

This repository is the source code and dashboard backing an E156 micro-paper on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

---

## `[131]` TruthCert PairwisePro: Browser-Based Pairwise Meta-Analysis with Regional Health-Economic Overlays

**Type:** methods  |  ESTIMAND: Pooled effect size (OR/RR/MD/SMD)  
**Data:** 13 African countries, 7 disease groups, metafor validation benchmarks

### 156-word body

Can a unified browser application deliver production-grade pairwise meta-analysis across thirteen regional health-economic contexts simultaneously? TruthCert PairwisePro v1.0 is a 27,076-line single-file HTML application providing random-effects meta-analysis with DerSimonian-Laird, REML, and Paule-Mandel estimators, HKSJ adjustment, prediction intervals, and thirteen country-specific cost-effectiveness overlays for Africa-focused health technology assessment applications. The system implements forest plots, funnel plots, Egger regression, trim-and-fill, leave-one-out sensitivity, and cumulative meta-analysis with automated GRADE certainty assessment, all running client-side without server dependencies or installation. Pooled estimates matched R metafor within 0.0001 for tau-squared across all validation benchmarks, with 101 of 101 regression tests passing on the production bundle. Sensitivity analysis confirmed stable conclusions across all three heterogeneity estimators and both confidence interval methods for each benchmark dataset. This architecture demonstrates that a zero-installation browser tool can serve both statistical rigor and health-economic translation in resource-limited settings. Nonetheless, the limitation of fixed country-level cost parameters means site-specific pharmacoeconomic adaptation requires manual override by local analysts.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Pairwiseai
  Protocol:  https://github.com/mahmood726-cyber/Pairwiseai/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/pairwiseai/

References (topic pack: trial sequential analysis (TSA)):
  1. Wetterslev J, Thorlund K, Brok J, Gluud C. 2008. Trial sequential analysis may establish when firm evidence is reached in cumulative meta-analysis. J Clin Epidemiol. 61(1):64-75. doi:10.1016/j.jclinepi.2007.03.013
  2. Pogue JM, Yusuf S. 1997. Cumulating evidence from randomized trials: utilizing sequential monitoring boundaries for cumulative meta-analysis. Control Clin Trials. 18(6):580-593. doi:10.1016/S0197-2456(97)00051-2

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020 (methods-paper variant — reports on review corpus).

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Methods Note — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._