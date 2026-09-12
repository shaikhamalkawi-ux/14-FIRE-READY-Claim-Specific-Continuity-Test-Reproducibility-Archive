#!/usr/bin/env python3
"""SOCR serialization adapter for the claim-specific continuity test.

This adapter does not discover scientific meaning. It receives prespecified
relation states and sufficient routes, then deterministically serializes:
- least-specific (N, Pi) support envelope,
- continuity state,
- inclusion-minimal unresolved repair sets.

It serializes the existing continuity-test logic and is not a new claim-scoring method.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

VALID = {"verified", "unresolved", "failed"}

def _minimize_sets(sets):
    unique = []
    for s in sorted({frozenset(x) for x in sets}, key=lambda x: (len(x), sorted(x))):
        if not any(t < s for t in unique):
            unique.append(s)
    return [sorted(s) for s in unique]

def evaluate_routes(routes: List[List[str]], states: Dict[str, str], qualified: bool = False):
    """Evaluate monotone OR-of-AND sufficient routes under ternary evidence states."""
    if not routes:
        raise ValueError("At least one sufficient route is required")
    for role, st in states.items():
        if st not in VALID:
            raise ValueError(f"Invalid state for {role}: {st}")

    # Necessity=1 iff some sufficient route is already fully verified.
    fully_verified = [
        route for route in routes
        if all(states.get(role) == "verified" for role in route)
    ]
    necessity = int(bool(fully_verified))

    # Possibility=1 iff some route contains no failed role.
    possible_routes = [
        route for route in routes
        if all(states.get(role) != "failed" for role in route)
    ]
    possibility = int(bool(possible_routes))

    if necessity:
        continuity_state = "preserved_with_qualification" if qualified else "same_question_preserved"
    elif possibility:
        continuity_state = "pending_evidence"
    else:
        continuity_state = "question_changed"

    # Inclusion-minimal evidence repair applies only to currently possible routes.
    # A failed mandatory relation is not "repaired" by pretending it is merely missing.
    repair_candidates = []
    if possibility and not necessity:
        for route in possible_routes:
            missing = [role for role in route if states.get(role) == "unresolved"]
            if missing:
                repair_candidates.append(missing)
    minimal_repair = _minimize_sets(repair_candidates)

    return {
        "necessity": necessity,
        "possibility": possibility,
        "continuity_state": continuity_state,
        "minimal_repair": minimal_repair,
    }
