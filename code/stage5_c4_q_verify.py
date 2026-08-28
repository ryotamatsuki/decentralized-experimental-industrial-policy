"""Stage 5 verification for C4 with host-dependent information productivity.

One substantive modification only: q_i.
Seed: 20260828
"""
from __future__ import annotations

import random
import sympy as sp

E, H, mu, F, q1, q2 = sp.symbols("E H mu F q1 q2", positive=True)
k = 1 + mu
Delta = q1 - q2

D1 = sp.simplify((H + E * Delta) / k)
D2 = sp.simplify((H - E * Delta) / k)
U1 = sp.simplify((q1 * E + H) / k)
U2 = sp.simplify((q2 * E + H) / k)
S1 = sp.simplify((2 * q1 * E + H) / k)

assert sp.simplify(D1 - D2 - 2 * E * Delta / k) == 0
assert sp.simplify(D1 + D2 - 2 * H / k) == 0
assert sp.simplify(U1 - D1 - q2 * E / k) == 0
assert sp.simplify(U2 - D2 - q1 * E / k) == 0
assert sp.simplify(U2 - D1 + E * (q1 - 2 * q2) / k) == 0
assert sp.simplify(S1 - U1 - q1 * E / k) == 0
assert sp.simplify(sp.diff(D2, q1) + E / k) == 0

# Stage 4 exact nesting at q1=q2=1.
subs_stage4 = {q1: 1, q2: 1}
assert sp.simplify(D1.subs(subs_stage4) - H / k) == 0
assert sp.simplify(D2.subs(subs_stage4) - H / k) == 0
assert sp.simplify(U1.subs(subs_stage4) - (E + H) / k) == 0
assert sp.simplify(S1.subs(subs_stage4) - (2 * E + H) / k) == 0

# Mixed volunteer region.
B = H - k * F
A1 = q1 * E + B
A2 = q2 * E + B
p1 = sp.factor(2 * A2 / (A2 + q1 * E))
p2 = sp.factor(2 * A1 / (A1 + q2 * E))
pdiff = sp.factor(p2 - p1)
expected_pdiff = sp.factor(2 * E * (q1 - q2) / (E * (q1 + q2) + H - k * F))
assert sp.simplify(pdiff - expected_pdiff) == 0

P1 = sp.factor(p1 * (1 - p2) + sp.Rational(1, 2) * p1 * p2)
P2 = sp.factor(p2 * (1 - p1) + sp.Rational(1, 2) * p1 * p2)
assert sp.simplify((P2 - P1) - (p2 - p1)) == 0

W1 = 2 * q1 * E + H - k * F
W2 = 2 * q2 * E + H - k * F
assert sp.simplify(W1 - W2 - 2 * E * (q1 - q2)) == 0

print("D1 =", D1)
print("D2 =", D2)
print("U1 =", U1)
print("U2 =", U2)
print("S1 =", S1)
print("p1 =", p1)
print("p2 =", p2)
print("p2-p1 =", pdiff)

random.seed(20260828)
N = 300_000
counts: dict[str, int] = {}
violations: list[tuple] = []
mixed_violations: list[tuple] = []
mislocation_count = 0

for _ in range(N):
    e = random.uniform(0.01, 5.0)
    h = random.uniform(0.01, 5.0)
    m = random.uniform(0.01, 2.0)
    c = random.uniform(0.1, 10.0)
    v = random.uniform(0.0, 12.0)
    qa = random.uniform(0.2, 2.5)
    qb = random.uniform(0.2, 2.5)
    q_hi, q_lo = max(qa, qb), min(qa, qb)

    kk = 1 + m
    f = c - v
    dq = q_hi - q_lo
    d_hi = (h + e * dq) / kk
    d_lo = (h - e * dq) / kk
    u_hi = (q_hi * e + h) / kk
    u_lo = (q_lo * e + h) / kk
    s_hi = (2 * q_hi * e + h) / kk

    if f <= 0:
        if d_lo > 0:
            region = "private_contested"
            s = d_lo
            w_plan = 2 * q_hi * e + h - f
            w_dec = w_plan - m * s
            ok = s < h / kk + 1e-12 and abs((w_plan - w_dec) - m * s) < 1e-9
        else:
            region = "private_uncontested"
            ok = e * dq >= h - 1e-10

    elif f < u_hi:
        if d_lo > f:
            region = "induced_contested_overpay"
            s = d_lo
            w_plan = 2 * q_hi * e + h - kk * f
            w_dec = 2 * q_hi * e + h - f - m * s
            ok = s > f and abs((w_plan - w_dec) - m * (s - f)) < 1e-9
        else:
            region = "high_quality_minimum_support"
            ok = True

        if d_hi < f < u_lo:
            mislocation_count += 1
            if not (q_hi < 2 * q_lo + 1e-10):
                mixed_violations.append(("interval_condition", q_hi, q_lo, f, d_hi, u_lo))

            b = h - kk * f
            a_hi = q_hi * e + b
            a_lo = q_lo * e + b
            p_hi = 2 * a_lo / (a_lo + q_hi * e)
            p_lo = 2 * a_hi / (a_hi + q_lo * e)

            if not (0 < p_hi < 1 and 0 < p_lo < 1 and p_lo > p_hi):
                mixed_violations.append(("mixed_probabilities", p_hi, p_lo))

            host_hi = p_hi * (1 - p_lo) + 0.5 * p_hi * p_lo
            host_lo = p_lo * (1 - p_hi) + 0.5 * p_hi * p_lo
            if not host_lo > host_hi:
                mixed_violations.append(("host_bias", host_hi, host_lo))

            fund_hi = (1 - p_lo) * a_hi + p_lo * 0.5 * (a_hi + q_lo * e)
            wait_hi = p_lo * q_lo * e
            fund_lo = (1 - p_hi) * a_lo + p_hi * 0.5 * (a_lo + q_hi * e)
            wait_lo = p_hi * q_hi * e
            if abs(fund_hi - wait_hi) > 1e-9 or abs(fund_lo - wait_lo) > 1e-9:
                mixed_violations.append(("indifference", fund_hi, wait_hi, fund_lo, wait_lo))

            welfare_gap = (2 * q_hi * e + h - kk * f) - (2 * q_lo * e + h - kk * f)
            if abs(welfare_gap - 2 * e * dq) > 1e-9:
                mixed_violations.append(("welfare_gap", welfare_gap, 2 * e * dq))

    elif f < s_hi:
        region = "under_experimentation"
        local = q_hi * e + h - kk * f
        social = 2 * q_hi * e + h - kk * f
        ok = local < 1e-10 and social > -1e-10

    else:
        region = "no_trial_efficient"
        social = 2 * q_hi * e + h - kk * f
        ok = social <= 1e-10

    counts[region] = counts.get(region, 0) + 1
    if not ok:
        violations.append((region, e, h, m, c, v, q_hi, q_lo))

print("Main-region counts:", counts)
print("Mislocation pure-equilibrium region:", mislocation_count)
print("Analytical-condition violations:", len(violations))
print("Mixed-equilibrium violations:", len(mixed_violations))

assert sum(counts.values()) == N
assert not violations
assert not mixed_violations
