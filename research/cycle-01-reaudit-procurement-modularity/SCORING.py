"""Reproducible Stage-3 scoring for Cycle 1 re-audit.

Columns:
mechanism novelty, prior-art survival, strategic distinctiveness,
welfare content, industrial-policy relevance, theorem potential,
minimality, tractability, international generality.
"""

scores = {
    "M1": [16, 10, 11, 8, 9, 5, 4, 4, 3],
    "M2": [15, 10, 10, 8, 8, 5, 3, 4, 3],
    "M3": [15, 9, 11, 9, 9, 5, 3, 4, 3],
    "M4": [17, 11, 12, 8, 9, 5, 3, 3, 3],
    "M5": [16, 11, 11, 8, 8, 5, 3, 3, 3],
    "M6": [18, 12, 12, 9, 10, 6, 3, 3, 3],
}

for variant, components in scores.items():
    assert len(components) == 9
    print(variant, sum(components))
