"""Stage 4 verification for C4: competition to host a supplier launch trial.

Python 3.13.5 / SymPy 1.14.0
Seed: 20260828
"""
from __future__ import annotations

import random
import sympy as sp

E, H, mu, C, V, F = sp.symbols("E H mu C V F", nonnegative=True)
k = 1 + mu

T_H = sp.simplify(H / k)
T_L = sp.simplify((E + H) / k)
T_S = sp.simplify((2 * E + H) / k)
s_star = T_H

W_private = sp.simplify(2 * E + H - F)
W_decentralized_bid = sp.simplify(W_private - mu * s_star)
W_targeted = sp.simplify(2 * E + H - k * F)
rent = sp.simplify(s_star - F)
excess_loss = sp.simplify(W_targeted - W_decentralized_bid)

D = sp.simplify(H - k * F)
q = sp.factor(2 * (E + D) / (2 * E + D))
p_trial = sp.factor(1 - (1 - q) ** 2)

assert sp.simplify(T_L - T_H - E / k) == 0
assert sp.simplify(T_S - T_L - E / k) == 0
assert sp.simplify(excess_loss - mu * (s_star - F)) == 0

print("Thresholds")
print("T_H =", T_H)
print("T_L =", T_L)
print("T_S =", T_S)
print("Equilibrium host bid s* =", s_star)
print("Targeted-vs-bidding welfare difference =", sp.factor(excess_loss))
print("Volunteer mixed funding probability q =", q)
print("Volunteer mixed trial probability =", p_trial)


def classify(e: float, h: float, m: float, c: float, v: float) -> str:
    kk = 1 + m
    f = c - v
    if f <= 0:
        return "private_trial_host_race"
    if f < h / kk:
        return "induced_bidding_war"
    if f <= (e + h) / kk:
        return "minimum_local_support"
    if f < (2 * e + h) / kk:
        return "under_experimentation"
    return "no_trial_efficient"


random.seed(20260828)
N = 200_000
counts: dict[str, int] = {}
violations = []

for _ in range(N):
    e = random.uniform(0.01, 5.0)
    h = random.uniform(0.01, 5.0)
    m = random.uniform(0.01, 2.0)
    c = random.uniform(0.1, 10.0)
    v = random.uniform(0.0, 12.0)
    kk = 1 + m
    f = c - v
    region = classify(e, h, m, c, v)
    counts[region] = counts.get(region, 0) + 1

    if region == "private_trial_host_race":
        s = h / kk
        w0 = 2 * e + h - f
        wd = w0 - m * s
        ok = s > 0 and w0 > wd
    elif region == "induced_bidding_war":
        s = h / kk
        wd = 2 * e + h - f - m * s
        wt = 2 * e + h - kk * f
        ok = s > f and wt > wd and wd > 0
    elif region == "minimum_local_support":
        w = 2 * e + h - kk * f
        ok = w >= -1e-12 and e + h - kk * f >= -1e-12
    elif region == "under_experimentation":
        w = 2 * e + h - kk * f
        local = e + h - kk * f
        ok = w > 0 and local < 0
    else:
        w = 2 * e + h - kk * f
        ok = w <= 1e-12

    if not ok:
        violations.append((region, e, h, m, c, v))

print("Random audit counts:", counts)
print("Violations:", len(violations))
assert not violations

for _ in range(10_000):
    e = random.uniform(0.05, 5.0)
    h = random.uniform(0.05, 5.0)
    m = random.uniform(0.01, 2.0)
    kk = 1 + m
    lo = h / kk + 1e-6
    hi = (e + h) / kk - 1e-6
    if lo >= hi:
        continue
    f = random.uniform(lo, hi)
    d = h - kk * f
    qq = 2 * (e + d) / (2 * e + d)
    assert 0 < qq < 1
    u_fund = (1 - qq) * (e + d) + qq * (e + d / 2)
    u_wait = qq * e
    assert abs(u_fund - u_wait) < 1e-10

print("Volunteer mixed-strategy indifference audit: PASS")
