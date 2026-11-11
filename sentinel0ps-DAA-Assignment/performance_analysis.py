
import math
import random
import time

def brute_force(events):
    min_dist = float('inf')
    pair = None
    comparisons = 0

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            comparisons += 1
            d = math.sqrt(
                (events[i][0] - events[j][0]) ** 2 +
                (events[i][1] - events[j][1]) ** 2
            )
            if d < min_dist:
                min_dist = d
                pair = (i, j)

    return pair, min_dist, comparisons

def optimized_closest_pair(events):
    min_dist_sq = float('inf')
    pair = None
    comparisons = 0

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            comparisons += 1
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            d_sq = dx * dx + dy * dy

            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                pair = (i, j)

    if pair is None:
        return None, float('inf'), comparisons

    return pair, math.sqrt(min_dist_sq), comparisons

random.seed(42)
sizes = [1000, 2000, 4000, 8000]

print("PERFORMANCE COMPARISON")
print("-" * 90)
print(f"{'N':<8}{'Brute Time (s)':<18}{'Optimized Time (s)':<22}{'Brute Ops':<18}{'Optimized Ops'}")

for n in sizes:
    events = [
        (random.randint(0, 10000), random.randint(0, 10000))
        for _ in range(n)
    ]

    start = time.perf_counter()
    brute_pair, brute_dist, brute_ops = brute_force(events)
    brute_time = time.perf_counter() - start

    start = time.perf_counter()
    opt_pair, opt_dist, opt_ops = optimized_closest_pair(events)
    opt_time = time.perf_counter() - start

    assert brute_pair == opt_pair
    assert math.isclose(brute_dist, opt_dist)

    print(f"{n:<8}{brute_time:<18.4f}{opt_time:<22.4f}{brute_ops:<18}{opt_ops}")
  