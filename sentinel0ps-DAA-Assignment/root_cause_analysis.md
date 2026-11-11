# Part B: Root Cause Analysis and Systematic Debugging

## 1. Introduction

The original SentinelOps program contained errors in four algorithms: Insertion Sort, Sequential Search, Brute-Force String Matching, and Brute-Force Closest Pair.

I examined the original code, identified the causes of the incorrect behavior, corrected the functions, and tested the results.

## 2. Root Cause Analysis

### 2.1 Insertion Sort: sort_alerts()

Problem 1: Incorrect loop boundary

Original code:
while j > 0 and alerts[j][1] < key[1]:

Root cause:
The condition j > 0 prevents the algorithm from comparing the element at index 0.

Correction:
while j >= 0 and alerts[j][1] < key[1]:

Problem 2: Incorrect insertion position

Original code:
alerts[j] = key

Root cause:
After shifting elements, the key must be inserted at index j + 1. Using index j can overwrite an element and produce incorrect sorting.

Correction:
alerts[j + 1] = key

Verification:
The corrected algorithm sorted the alerts in descending order of severity.

## 2.2 Sequential Search: is_blocked()

Problem 1: Incorrect return value

Original code:
if blocklist[i] == ip:
    return False

Root cause:
The function returns False even when the IP address is present in the blocklist.

Correction:
Return True when a matching IP is found.

Problem 2: Premature termination

Original code:
else:
    return False

Root cause:
The search stops after the first non-matching IP address instead of checking the remaining entries.

Correction:
Move return False outside the loop.

Verification:
The corrected function returned True for a blocked IP and False for an IP not found in the blocklist.

## 2.3 String Matching: find_signature()

Problem 1: Undefined expression

Original code:
occurrences

Root cause:
The expression refers to a variable that has not been defined, causing a NameError when the function executes.

Correction:
Remove the unnecessary expression.

Problem 2: Incorrect search range

Original code:
for i in range(n - m):

Root cause:
The final possible starting position is excluded, so a valid match at the end of the log can be missed.

Correction:
for i in range(n - m + 1):

Problem 3: Incorrect match validation

Original code:
if j == m - 1:
    hits.append(i)

Root cause:
The loop index can reach m - 1 even when the last character does not match. This may produce a false positive.

Correction:
Verify that the entire pattern matches before recording the starting index.

Verification:
The corrected algorithm detected valid matches, including overlapping occurrences.

## 2.4 Closest Pair: closest_logins()

Problem 1: Undefined expression

Original code:
locations

Root cause:
The expression refers to an undefined variable and causes a NameError.

Correction:
Remove the unnecessary expression.

Problem 2: Incorrect minimum distance initialization

Original code:
min_dist = 0

Root cause:
Zero is not a suitable initial minimum when searching for the smallest distance among distinct events.

Correction:
min_dist = float('inf')

Problem 3: Repeated and self-comparisons

Original code:
for j in range(len(events)):

Root cause:
The algorithm compares each event with itself and examines the same pair in both directions.

Correction:
for j in range(i + 1, len(events)):

Problem 4: Incorrect comparison operator

Original code:
if d > min_dist:

Root cause:
The condition selects larger distances rather than the smallest distance.

Correction:
if d < min_dist:

Verification:
The corrected function returned the expected closest pair and Euclidean distance.

## 3. Systematic Debugging Method

The debugging process followed these steps:

1. Inspect the original functions.
2. Identify incorrect conditions, indices, and return statements.
3. Correct one function at a time.
4. Run the corrected code using the available test cases.
5. Compare the actual results with the expected results.
6. Verify that the corrections preserve the intended algorithms.

## 4. Conclusion

The main causes of the defects were incorrect loop boundaries, wrong return statements, invalid index placement, incomplete match validation, incorrect distance comparison, and undefined expressions.

By correcting these issues and testing the functions, the SentinelOps module produced the expected results for the recorded test cases.
## 5. Before-and-After Debugging Trace

### Example 1: Sequential Search

Input:
blocklist = ["10.0.0.5", "10.0.0.9"]
ip = "10.0.0.9"

Original execution:
1. Compare "10.0.0.5" with "10.0.0.9".
2. The first comparison does not match.
3. The function immediately returns False.
4. The second IP is never checked.

Original result: False (incorrect)

Corrected execution:
1. Compare "10.0.0.5" with "10.0.0.9".
2. No match, so continue searching.
3. Compare "10.0.0.9" with "10.0.0.9".
4. A match is found, so return True.

Corrected result: True (expected)

### Example 2: String Matching

Input:
log = "ABCDEF"
pattern = "DEF"

Original execution:
1. n = 6 and m = 3.
2. The original range is range(3).
3. Only starting positions 0, 1, and 2 are checked.
4. The valid match at position 3 is skipped.

Corrected execution:
1. The range becomes range(4).
2. Starting positions 0, 1, 2, and 3 are checked.
3. The pattern "DEF" matches at position 3.

Corrected result: [3]

### Example 3: Closest Pair

Input:
events = [(0, 0), (3, 4), (1, 1)]

Original logic:
1. Minimum distance starts at 0.
2. The algorithm compares events with themselves.
3. It uses the condition d > min_dist.
4. This selects larger distances instead of the minimum.

Corrected logic:
1. Minimum distance starts at infinity.
2. Only distinct pairs are compared.
3. Distances are calculated for each pair.
4. The smallest distance is selected.

Corrected result:
Pair: (0, 2)
Distance: 1.4142135623730951

## 6. Debugging Verification

The corrected algorithms were tested using the available test inputs. The recorded results matched the expected outputs.

The debugging process demonstrates how incorrect conditions and loop boundaries affected the program and how the corrections resolved the identified problems.