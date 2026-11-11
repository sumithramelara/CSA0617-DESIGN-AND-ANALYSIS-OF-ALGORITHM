# Part D: Before-and-After Performance Analysis

## 1. Objective

The objective of this experiment is to compare the execution time and computational complexity of the corrected brute-force closest-pair algorithm and its optimized version.

## 2. Experimental Method

Both algorithms were tested using input sizes of 1,000, 2,000, 4,000, and 8,000 login events.

The corrected algorithm calculates Euclidean distance for each pair, while the optimized algorithm compares squared distances and performs a square-root calculation only for the final result.

Both algorithms examine n(n - 1)/2 pairs.

## 3. Experimental Results

| Input Size | Corrected Time (s) | Optimized Time (s) | Pair Comparisons |
|---|---|---|---|
| 1,000 | 0.2756 | 0.1167 | 499,500 |
| 2,000 | 0.7480 | 0.5019 | 1,999,000 |
| 4,000 | 2.8672 | 1.6143 | 7,998,000 |
| 8,000 | 10.8839 | 6.6834 | 31,996,000 |

## 4. Performance Improvement

For 8,000 events:

Corrected execution time = 10.8839 seconds

Optimized execution time = 6.6834 seconds

Time saved = 4.2005 seconds

Percentage improvement:

(4.2005 / 10.8839) × 100 = 38.59%

The optimized version completed the 8,000-event test approximately 38.6% faster.

## 5. Complexity Analysis

Corrected Algorithm:
Time Complexity = O(n²)
Space Complexity = O(1)

Optimized Algorithm:
Time Complexity = O(n²)
Space Complexity = O(1)

Both algorithms examine the same number of event pairs.

The optimized version improves execution time by avoiding repeated square-root calculations, not by reducing the number of comparisons.

## 6. Observations

1. Execution time increased as the number of events increased.
2. The optimized algorithm was faster for all four tested input sizes.
3. Both algorithms performed the same number of pair comparisons.
4. The improvement was achieved by reducing computational overhead.
5. The benchmark results are specific to the test environment and may vary across different systems.

## 7. Evidence

The benchmark output screenshot is saved at:

screenshots/performance_comparison.png

The benchmark program is available in:

performance_analysis.py

## 8. Conclusion

The experimental results demonstrate that the optimized closest-pair algorithm executes faster than the corrected brute-force implementation for the tested input sizes.

Although both algorithms have O(n²) time complexity, avoiding repeated square-root calculations produced a measurable performance improvement.