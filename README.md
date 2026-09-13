# 🔥 FIRE READY — Claim-Specific Continuity Test

Reproducibility repository for the manuscript:

**When Data Substitution Changes the Scientific Question: An Evidence-Admissibility Test for Wildfire Robustness Analysis**

This repository supports deterministic replay of the claim-continuity serialization reported in the manuscript. It includes the benchmark registry, release predicates, SOCR schema/examples, prespecified OR-of-AND rule registry, conformance/metamorphic tests, rule-to-record validation, and the **blinded semantic-coding packet prepared for future independent recoding**.

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability or external validation. Independent semantic recoding has not been completed and no inter-rater agreement statistic is claimed.

## Run the verification

```bash
bash run_all.sh
```

Expected result:

- **15/15** conformance/metamorphic tests PASS
- **5/5** rule-to-record derivations PASS

## Scientific interpretation

A reproducible replacement result is not automatically admissible robustness evidence. The replacement must preserve the scientific object that defines the registered claim. Numerical magnitude does not compensate for a failed mandatory scientific relation.

The canonical journal-supplied reproducibility ZIP remains the frozen archival package; this repository provides a directly inspectable public mirror of the code and text artifacts.

## Persistent archive and citation

The unchanged canonical reproducibility ZIP is archived in Zenodo, version **149R4**.

- Version DOI: [10.5281/zenodo.22730737](https://doi.org/10.5281/zenodo.22730737)
- All-versions DOI: [10.5281/zenodo.22730736](https://doi.org/10.5281/zenodo.22730736)
- [Published archive record](https://zenodo.org/records/22730737)

This is a direct Zenodo deposit. It contains only `Reproducibility_Archive.zip` and `LICENSES_AND_RIGHTS.txt`; no GitHub release/tag was used. The scientific-material mirror was verified at commit `48d8bec070b47829b5ea8a85b35e87f02e67cb7f`.

## Licenses and third-party rights

The authors have approved **MIT** for their original software and **CC BY 4.0** for their original documentation and data contributions for which they own the rights. See [LICENSES_AND_RIGHTS.txt](LICENSES_AND_RIGHTS.txt) for the file-by-file scope and full MIT terms.

Third-party materials and external-source excerpts retain their original rights and are excluded from these license grants. Source-reported values and references do not imply ownership of the underlying publications or datasets.
