# 🔥 FIRE READY — Claim-Specific Continuity Test

Reproducibility repository for the manuscript:

**When Data Substitution Changes the Scientific Question: Claim-Level Evidence Admissibility in Wildfire Robustness Analysis**

This repository supports deterministic replay of the claim-continuity serialization reported in the manuscript. It includes the benchmark registry, release predicates, SOCR schema/examples, prespecified OR-of-AND rule registry, conformance/metamorphic tests, rule-to-record validation, and the blinded semantic-coding packet.

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability or external validation.

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
