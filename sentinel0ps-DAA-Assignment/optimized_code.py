import math 
  
def sort_alerts(alerts):
    if len(alerts) < 2:
        return alerts

    max_index = max(range(len(alerts)), key=lambda i: alerts[i][1])
    alerts[0], alerts[max_index] = alerts[max_index], alerts[0]

    for i in range(2, len(alerts)):
        key = alerts[i]
        j = i - 1
        while alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j + 1] = key

    return alerts
  
def is_blocked(blocklist, ip):
    return ip in blocklist
  
def find_signature(log, pattern):
    n, m = len(log), len(pattern)
    hits = []

    if m == 0:
        return hits

    for i in range(n - m + 1):
        match = True

        for j in range(m):
            if log[i + j] != pattern[j]:
                match = False
                break

        if match:
            hits.append(i)

    return hits
  
def closest_logins(events):
    min_dist_sq = float('inf')
    pair = None

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            d_sq = dx ** 2 + dy ** 2

            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                pair = (i, j)

    if pair is None:
        return None, float('inf')

    return pair, math.sqrt(min_dist_sq)
test_alerts = [
    ("A1", 2),
    ("A2", 5),
    ("A3", 1),
    ("A4", 4)
]

print("Before sorting:", test_alerts)
print("After sorting:", sort_alerts(test_alerts.copy()))
blocklist = ["10.0.0.5", "10.0.0.9", "192.16.4.2"]

print("Test 1:", is_blocked(blocklist, "10.0.0.9"))
print("Test 2:", is_blocked(blocklist, "10.0.0.8"))
print("Test 3:", is_blocked([], "10.0.0.5"))
print("\nSTRING MATCHING TESTS")

print("Test 1:", find_signature("ABCDEF", "DEF"))
print("Test 2:", find_signature("ABABA", "ABA"))
print("Test 3:", find_signature("HELLO", "XYZ"))
print("Test 4:", find_signature("ABC", "ABCDE"))
print("\nCLOSEST PAIR TESTS")

events = [(0, 0), (3, 4), (1, 1), (10, 10)]

print("Test 1:", closest_logins(events))
print("Test 2:", closest_logins([(0, 0), (3, 4)]))
print("Test 3:", closest_logins([(1, 1)]))
print("\nOPTIMIZED BLOCKLIST TEST")

blocked_ips = {"10.0.0.5", "10.0.0.9", "192.16.4.2"}

print("Test 1:", is_blocked(blocked_ips, "10.0.0.9"))
print("Test 2:", is_blocked(blocked_ips, "10.0.0.8"))
print("Test 3:", is_blocked(set(), "10.0.0.5"))
