import math 
  
def sort_alerts(alerts):            # insertion sort by severity, highest first 
    for i in range(1, len(alerts)): 
        key = alerts[i] 
        j = i - 1 
        while j >= 0 and alerts[j][1] < key[1]: 
            alerts[j + 1] = alerts[j] 
            j -= 1 
        alerts[j+1] = key 
    return alerts 
  
def is_blocked(blocklist, ip):      # sequential search 
    for i in range(len(blocklist)): 
        if blocklist[i] == ip: 
            return True 
    return False 
  
def find_signature(log, pattern):   # brute-force string matching, all 
    occurrences = []
    n, m = len(log), len(pattern) 
    hits = [] 
    for i in range(n - m+1): 
        for j in range(m): 
            if log[i + j] != pattern[j]: 
                break 
        if log[i:i+m] == pattern: 
            hits.append(i) 
    return hits 
  
def closest_logins(events):         # brute-force closest pair of login  
    min_dist = float('inf')
    pair = None 
    for i in range(len(events)): 
        for j in range(i+1,len(events)): 
            d = math.sqrt((events[i][0] - events[j][0]) ** 2 + 
                          (events[i][1] - events[j][1]) ** 2) 
            if d < min_dist: 
                min_dist = d 
                pair = (i, j) 
    return pair, min_dist
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