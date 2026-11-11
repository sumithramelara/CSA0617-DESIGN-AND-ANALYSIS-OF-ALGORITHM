# Part C: Algorithm Optimization Analysis

## 1. Introduction

After correcting the defects in the SentinelOps module, I optimized the algorithms to reduce unnecessary operations and improve execution efficiency.

## 2. Insertion Sort Optimization

Algorithm: Sentinel Insertion Sort

The corrected insertion sort checks the array boundary during comparisons.

In the optimized version, an alert with maximum severity is placed at the beginning as a sentinel. This removes repeated boundary checks inside the insertion loop.

Time Complexity:
Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)

The optimization reduces comparison overhead but does not change the worst-case time complexity.

Note: The sentinel implementation may change the relative order of alerts with equal severity.

## 3. Blocked-IP Search Optimization

Algorithm: Hash-Based Searching

The corrected version uses sequential search to check whether an IP address exists in the blocklist.

The optimized version uses a Python set for repeated membership checks.

Sequential Search: O(n) per lookup
Set Construction: O(n) average
Set Lookup: O(1) average

The hash-based approach is useful when many IP addresses must be checked against the same blocklist.

## 4. String Matching Optimization

Algorithm: Improved Brute-Force String Matching

The optimized algorithm compares characters sequentially and stops immediately when a mismatch is found.

It also removes the unnecessary second comparison of the entire substring.

Worst-Case Time Complexity: O(nm)

Here:
n = Length of the log
m = Length of the pattern

The optimization reduces redundant comparisons while preserving overlapping matches.

## 5. Closest Pair Optimization

Algorithm: Squared-Distance Comparison

The corrected brute-force algorithm calculates Euclidean distance using a square root for every pair.

The optimized version compares squared distances and calculates the square root only once for the final closest pair.

Original Time Complexity: O(n²)
Optimized Time Complexity: O(n²)

Both versions examine the same number of pairs. The optimization reduces computational overhead rather than the asymptotic time complexity.

## 6. Conclusion

The optimizations improve the efficiency of the SentinelOps module by reducing unnecessary comparisons, using hash-based lookups, and avoiding repeated square-root calculations.

The algorithms were designed to preserve the expected results for the tested inputs.