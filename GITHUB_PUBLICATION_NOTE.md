# FIRE READY - Claim-Specific Continuity Test

This public repository accompanies the manuscript:

**When Data Substitution Changes the Scientific Question: Claim-Level Evidence Admissibility in Wildfire Robustness Analysis**

It contains the locked reproducibility archive for the claim-specific continuity test: benchmark and release-contract registries, SOCR schema/examples, deterministic conformance and metamorphic tests, rule-to-record validation, and the blinded semantic-recoding packet.

## Scientific boundary

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability, external validation, or a generic ranking/scoring framework.

## Reproduce

```bash
bash run_all.sh
sha256sum -c SHA256SUMS.txt
```

Expected: **15/15** conformance/metamorphic tests PASS and **5/5** rule-to-record derivations PASS.

## Public repository

https://github.com/shaikhamalkawi-ux/14-FIRE-READY-Claim-Specific-Continuity-Test-Reproducibility-Archive

No software license is assigned by this publication step; license selection remains an author decision.
