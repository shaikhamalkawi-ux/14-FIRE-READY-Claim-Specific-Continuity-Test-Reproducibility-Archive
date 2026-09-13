# Reproducibility Archive

Reproducibility repository for the manuscript:

**When Data Substitution Changes the Scientific Question: An Evidence-Admissibility Test for Wildfire Robustness Analysis**

This repository supports deterministic replay of the claim-specific continuity test reported in the manuscript. It includes the benchmark registry, release predicates, SOCR schema/examples, prespecified OR-of-AND rule registry, conformance/metamorphic tests, rule-to-record validation, and the **blinded semantic-coding packet prepared for future independent recoding**.

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish independent-coder semantic reliability or external validation. Independent semantic recoding has not been completed, and no inter-rater agreement statistic is claimed.

## Run the verification

```bash
bash run_all.sh
```

Expected result:

- **15/15** conformance/metamorphic tests PASS
- **5/5** rule-to-record derivations PASS

## Scientific interpretation

A reproducible replacement result is not automatically admissible robustness evidence. The replacement must preserve the scientific object that defines the registered claim. Numerical magnitude does not compensate for a failed mandatory scientific relation.

## Persistent archive and citation

The archived reproducibility materials are available from Zenodo:

- Version DOI: [10.5281/zenodo.22730737](https://doi.org/10.5281/zenodo.22730737)
- All-versions DOI: [10.5281/zenodo.22730736](https://doi.org/10.5281/zenodo.22730736)
- [Zenodo record](https://zenodo.org/records/22730737)

This GitHub repository provides a directly inspectable mirror of the text and code artifacts associated with the archived deposit.

## Licenses and third-party rights

The original software is released under the **MIT License**. Original documentation and data contributions for which the authors hold the relevant rights are released under **CC BY 4.0**. See [LICENSES_AND_RIGHTS.txt](LICENSES_AND_RIGHTS.txt) for file-level scope and the full MIT terms.

Third-party materials and external-source excerpts retain their original rights and are excluded from these license grants. Source-reported values and references do not imply ownership of the underlying publications or datasets.
