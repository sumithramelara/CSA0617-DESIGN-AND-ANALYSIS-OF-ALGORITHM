# SentinelOps: Debugging and Algorithm Optimization

## Design and Analysis of Algorithms Assignment

### Project Overview

SentinelOps is a Python-based project focused on identifying, debugging, correcting, and optimizing algorithms used in a security-monitoring system.

The project covers four algorithms:

1. Insertion Sort for sorting security alerts.
2. Sequential Search for checking blocked IP addresses.
3. Brute-Force String Matching for detecting signatures in logs.
4. Brute-Force Closest Pair for analyzing login-event locations.

## Project Objectives

- Identify defects in the original algorithms.
- Explain the root causes of incorrect behavior.
- Correct the algorithms.
- Verify the corrected implementations using test cases.
- Optimize the algorithms.
- Compare execution times and computational complexity.
- Document the debugging and optimization process.

## Project Files

| File | Description |
|---|---|
| original_code.py | Original code containing defects |
| corrected_code.py | Corrected algorithm implementations |
| optimized_code.py | Optimized algorithm implementations |
| performance_analysis.py | Performance benchmarking program |
| defect_analysis.md | Defect identification and test results |
| root_cause_analysis.md | Root cause analysis and debugging traces |
| optimization_analysis.md | Explanation of algorithm optimizations |
| performance_report.md | Benchmark results and complexity analysis |
| performance_comparison.png | Benchmark output screenshot |

## Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor

The project uses Python's standard library.

## How to Run

Open a terminal in the project folder.

Run the corrected algorithms:

```bash
python corrected_code.py
```

Run the optimized algorithms:

```bash
python optimized_code.py
```

Run the performance benchmark:

```bash
python performance_analysis.py
```

## Performance Summary

For 8,000 login events:

- Corrected implementation: 10.8839 seconds
- Optimized implementation: 6.6834 seconds
- Execution-time reduction: approximately 38.6%

Both closest-pair implementations have O(n²) time complexity.

## Conclusion

The SentinelOps project demonstrates systematic debugging, algorithm correction, optimization, and performance analysis.

The recorded tests verified the corrected implementations, while the benchmark demonstrated improved execution efficiency for the optimized closest-pair algorithm.
