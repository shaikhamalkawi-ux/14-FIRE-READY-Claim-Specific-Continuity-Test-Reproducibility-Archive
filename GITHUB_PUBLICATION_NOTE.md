# FIRE READY - Claim-Specific Continuity Test

This public repository accompanies the manuscript:

**When Data Substitution Changes the Scientific Question: An Evidence-Admissibility Test for Wildfire Robustness Analysis**

It mirrors the executable and human-readable reproducibility artifacts for the claim-specific continuity test: benchmark and release-contract registries, SOCR schema/examples, deterministic conformance and metamorphic tests, rule-to-record validation, and the **blinded semantic-coding packet prepared for future independent recoding**.

## Scientific boundary

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability, external validation, or a generic ranking/scoring framework. Independent semantic recoding has not been completed and no inter-rater agreement statistic is claimed.

## Reproduce

```bash
bash run_all.sh
```

Expected: **15/15** conformance/metamorphic tests PASS and **5/5** rule-to-record derivations PASS.

## Archive status

The journal-supplied reproducibility ZIP remains the canonical frozen package and contains its SHA-256 manifest. This GitHub repository is the public, directly inspectable mirror of the text/code artifacts. Formatting-only JSON serialization differences in the public mirror do not change the registered rules or scientific results.

The canonical ZIP is preserved in Zenodo, version 149R4: https://doi.org/10.5281/zenodo.22730737 (concept DOI: https://doi.org/10.5281/zenodo.22730736). This direct deposit contains only the unchanged reproducibility ZIP and its accompanying rights notice.

The authors approved MIT for their original software and CC BY 4.0 for their original documentation/data contributions for which they own the rights. See LICENSES_AND_RIGHTS.txt for the file-level scope. Third-party material and external-source excerpts retain their original rights and are excluded from these grants.
