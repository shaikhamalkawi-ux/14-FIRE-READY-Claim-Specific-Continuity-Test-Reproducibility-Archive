# Publication and archive note

This public repository accompanies the manuscript:

**When Data Substitution Changes the Scientific Question: An Evidence-Admissibility Test for Wildfire Robustness Analysis**

It mirrors the executable and human-readable reproducibility artifacts for the claim-specific continuity test: benchmark and release-contract registries, SOCR schema/examples, deterministic conformance and metamorphic tests, rule-to-record validation, and the **blinded semantic-coding packet prepared for future independent recoding**.

## Scientific boundary

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish independent-coder semantic reliability, external validation, or a generic ranking/scoring framework. Independent semantic recoding has not been completed, and no inter-rater agreement statistic is claimed.

## Reproduce

```bash
bash run_all.sh
```

Expected: **15/15** conformance/metamorphic tests PASS and **5/5** rule-to-record derivations PASS.

## Archived record

The reproducibility materials are preserved in Zenodo at https://doi.org/10.5281/zenodo.22730737 (all-versions DOI: https://doi.org/10.5281/zenodo.22730736). The Zenodo deposit contains the reproducibility archive and its accompanying rights notice.

This GitHub repository provides a directly inspectable version of the text and code artifacts. Minor wording or serialization cleanup in the public mirror does not change the registered rules, numerical results, or scientific conclusions.

The original software is released under MIT, and original documentation/data contributions for which the authors hold the relevant rights are released under CC BY 4.0. See `LICENSES_AND_RIGHTS.txt` for the file-level scope. Third-party materials and external-source excerpts retain their original rights and are excluded from these grants.
