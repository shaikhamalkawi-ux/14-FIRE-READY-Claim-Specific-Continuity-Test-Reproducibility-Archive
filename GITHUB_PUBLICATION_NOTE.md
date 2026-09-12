# FIRE READY - Claim-Specific Continuity Test

This public repository accompanies the manuscript:

**When Data Substitution Changes the Scientific Question: Claim-Level Evidence Admissibility in Wildfire Robustness Analysis**

It mirrors the executable and human-readable reproducibility artifacts for the claim-specific continuity test: benchmark and release-contract registries, SOCR schema/examples, deterministic conformance and metamorphic tests, rule-to-record validation, and the blinded semantic-recoding packet.

## Scientific boundary

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability, external validation, or a generic ranking/scoring framework.

## Reproduce

```bash
bash run_all.sh
```

Expected: **15/15** conformance/metamorphic tests PASS and **5/5** rule-to-record derivations PASS.

## Archive status

The journal-supplied reproducibility ZIP remains the canonical frozen package and contains its SHA-256 manifest. This GitHub repository is the public, directly inspectable mirror of the text/code artifacts. Formatting-only JSON serialization differences in the public mirror do not change the registered rules or scientific results.

No software license has been assigned by this publication step; license selection remains an author decision.
