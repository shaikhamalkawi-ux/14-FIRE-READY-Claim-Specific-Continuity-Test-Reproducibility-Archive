# Reproducibility archive

This archive supports deterministic replay of the claim-continuity serialization reported in the manuscript. It contains the primary benchmark registry, release predicates, SOCR schema/examples, a prespecified OR-of-AND rule registry, conformance tests, rule-to-record validation, and a blinded semantic-coding packet.

The executable checks verify internal consistency **conditional on the registered evidence-state coding**. They do not establish observer-independent semantic reliability or external validation.

Run: `bash run_all.sh` (Python 3; `jsonschema` is used when installed and a structural fallback is used otherwise).

Expected: 15/15 conformance/metamorphic tests PASS and 5/5 rule-to-record derivations PASS.
