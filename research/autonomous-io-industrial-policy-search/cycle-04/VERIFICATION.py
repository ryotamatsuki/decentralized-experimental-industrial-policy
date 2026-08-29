"""Cycle 04 Stage 4 verification.

Frozen mechanism: a public pilot creates a verifiable state signal and a
supplier-specific learning advantage; government releases the signal early
or late; a potential entrant chooses entry before later competition.

This script deliberately tests whether the timing effect survives after the
learning primitive is removed.  No rescue primitive is added.
"""

from itertools import product


def q_early(p, vh, vl, F, b, x):
    """Entrant entry probability when the state is publicly revealed early."""
    return p * int(vh - F - b * x >= 0) + (1 - p) * int(
        vl - F - b * x >= 0
    )


def q_late(p, vh, vl, F, b, x):
    """Entrant entry probability when only the prior is available."""
    return int(p * (vh - b * x) + (1 - p) * (vl - b * x) - F >= 0)


def welfare_early(p, GH, GL, vh, vl, F, b=0.0, x=0):
    return (
        p * int(vh - F - b * x >= 0) * GH
        + (1 - p) * int(vl - F - b * x >= 0) * GL
    )


def welfare_late(p, GH, GL, vh, vl, F, b=0.0, x=0):
    return (p * GH + (1 - p) * GL) * q_late(p, vh, vl, F, b, x)


def main():
    regions = {
        "early_less_entry": (0.5, 0.9, 0.1, 0.4, 0.0, 0),
        "early_more_entry": (0.5, 0.9, 0.1, 0.6, 0.0, 0),
        "learning_turns_off_late": (0.5, 0.9, 0.1, 0.4, 0.2, 1),
    }
    for name, args in regions.items():
        print(
            name,
            "early=",
            q_early(*args),
            "late=",
            q_late(*args),
        )

    counts = {
        "same_one": 0,
        "early_p_late_one": 0,
        "early_p_late_zero": 0,
        "same_zero": 0,
    }
    grid = product(
        (0.25, 0.5, 0.75),
        (0.8, 1.0),
        (0.1, 0.2),
        (0.05, 0.15, 0.35, 0.55, 0.75, 0.95),
        (0.0, 0.1, 0.2),
        (0, 1),
    )
    for p, vh, vl, F, b, x in grid:
        e = q_early(p, vh, vl, F, b, x)
        l = q_late(p, vh, vl, F, b, x)
        vbar = p * vh + (1 - p) * vl
        effective_cost = F + b * x
        if effective_cost <= vl:
            expected = "same_one"
            expected_pair = (1, 1)
        elif effective_cost <= vbar:
            expected = "early_p_late_one"
            expected_pair = (p, 1)
        elif effective_cost <= vh:
            expected = "early_p_late_zero"
            expected_pair = (p, 0)
        else:
            expected = "same_zero"
            expected_pair = (0, 0)
        counts[expected] += 1
        assert (e, l) == expected_pair
    print("cutoff_region_grid_counts", counts)

    # The timing effect remains after the learning primitive is removed.
    p, vh, vl, F = 0.5, 0.9, 0.1, 0.4
    assert q_early(p, vh, vl, F, 0.0, 0) == 0.5
    assert q_late(p, vh, vl, F, 0.0, 0) == 1
    print(
        "learning_removed",
        "early=",
        q_early(p, vh, vl, F, 0.0, 0),
        "late=",
        q_late(p, vh, vl, F, 0.0, 0),
    )

    # Welfare ranking reverses without changing the information structure.
    case_a = (
        welfare_early(0.5, 1.0, 1.0, 0.9, 0.1, 0.4),
        welfare_late(0.5, 1.0, 1.0, 0.9, 0.1, 0.4),
    )
    case_b = (
        welfare_early(0.5, 1.0, -0.2, 0.9, 0.1, 0.4),
        welfare_late(0.5, 1.0, -0.2, 0.9, 0.1, 0.4),
    )
    assert case_a == (0.5, 1.0)
    assert case_b == (0.5, 0.4)
    print("welfare_sign_case_a", case_a)
    print("welfare_sign_case_b", case_b)

    # Degenerate information cases eliminate the release-timing effect.
    assert q_early(1.0, 0.9, 0.1, 0.4, 0.0, 0) == q_late(
        1.0, 0.9, 0.1, 0.4, 0.0, 0
    ) == 1
    assert q_early(0.5, 0.5, 0.5, 0.4, 0.0, 0) == q_late(
        0.5, 0.5, 0.5, 0.4, 0.0, 0
    ) == 1
    print("edge_cases", "degenerate_prior=1", "homogeneous_state=1")


if __name__ == "__main__":
    main()
