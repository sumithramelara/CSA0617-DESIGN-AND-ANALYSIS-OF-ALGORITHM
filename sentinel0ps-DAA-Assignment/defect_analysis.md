# Part A: Reproduce and Identify the Defects

## 1. Introduction

The SentinelOps module processes security alerts, checks blocked IP addresses, searches logs for attack signatures, and identifies the closest pair of login events.

The original program contained logical errors that affected the accuracy of its results. I tested the functions, identified incorrect behavior, and corrected the algorithms.

## 2. Defect Identification

| No. | Function | Original Defect | Correction |
|---|---|---|---|
| 1 | sort_alerts | Loop condition j > 0 skips index 0. | Use j >= 0. |
| 2 | sort_alerts | Key inserted at alerts[j]. | Insert at alerts[j + 1]. |
| 3 | is_blocked | Returns False when IP matches. | Return True when matched. |
| 4 | is_blocked | Returns False inside the loop. | Return False after the loop. |
| 5 | find_signature | Search range excludes the last position. | Use range(n - m + 1). |
| 6 | find_signature | Final-character mismatch can be reported as a match. | Verify the complete pattern before recording a match. |
| 7 | closest_logins | Minimum distance initialized to 0. | Initialize to infinity. |
| 8 | closest_logins | Self-comparisons and duplicate pairs occur. | Start inner loop at i + 1. |
| 9 | closest_logins | Uses d > min_dist. | Use d < min_dist. |

## 3. Additional Errors

The original code also contains two undefined expressions:

1. The standalone expression `occurrences` in find_signature.
2. The standalone expression `locations` in closest_logins.

These expressions cause NameError exceptions when their respective functions are executed.

## 4. Conclusion

The original SentinelOps module contained defects affecting sorting, blocked-IP searching, signature matching, and closest-pair detection. The corrected implementation addresses these issues and produces the expected results for the tested inputs.
## 5. Testing and Verification

After correcting the defects, the SentinelOps functions were tested using different inputs to verify their behavior.

### 5.1 Alert Sorting

Input:
[("A1", 2), ("A2", 5), ("A3", 1), ("A4", 4)]

Output:
[("A2", 5), ("A4", 4), ("A1", 2), ("A3", 1)]

The alerts were correctly sorted in descending order of severity.

### 5.2 Blocked IP Search

The corrected sequential search returned True for a blocked IP and False for an IP not present in the blocklist.

The function also returned False for an empty blocklist.

### 5.3 Signature Matching

Test 1: "ABCDEF", "DEF" -> [3]
Test 2: "ABABA", "ABA" -> [0, 2]
Test 3: "HELLO", "XYZ" -> []
Test 4: "ABC", "ABCDE" -> []

The corrected function identified valid signatures, including overlapping matches, and returned an empty list when no match existed.

### 5.4 Closest Pair of Login Events

Test 1:
Input: [(0, 0), (3, 4), (1, 1)]
Result: ((0, 2), 1.4142135623730951)

Test 2:
Input: [(0, 0), (3, 4)]
Result: ((0, 1), 5.0)

Test 3:
Input: [(1, 1)]
Result: (None, inf)

The corrected algorithm identified the closest pair and calculated the Euclidean distance correctly.

## 6. Verification Summary

The corrected functions produced the expected results for the recorded test cases. These tests demonstrate that the identified defects were addressed for the tested inputs.