# Programming Assignment 2 - Greedy Algorithms

## Overview
Programming Assignment 2 implements and compares three cache eviction policies: FIFO (First-In, First-Out), LRU (Least Recently Used), and OPTFF (Belady's Farthest-in-Future, optimal offline), on the same sequence of cache requests. The program reads a cache capacity and request stream from an input file, simulates each policy, and outputs the number of cache misses for each one. The assignment also (1) empirically compares miss counts across multiple nontrivial inputs, (2) constructs and analyzes a bad request sequence for FIFO or LRU when k = 3, and (3) proves that OPTFF is optimal among offline algorithms, meaning it never produces more misses than any other offline strategy on the same request sequence.

## Students
- Student 1: Brock Gilman - UFID: 58803474
- Student 2: Kyle Scarmack - UFID: 20823723

## Repository Structure
- `src/main.py` - Program entry point with a menu to run FIFO, LRU, or OPTFF.
- `src/fifo.py` - FIFO cache simulation.
- `src/lru.py` - LRU cache simulation.
- `src/optff.py` - OPTFF cache simulation.
- `data/inputs/example.in` - Example input file.
- `data/outputs/example.out` - Expected output for `example.in`.

## Input / Output Format
### Input
Input files use:

```
k m
r1 r2 r3 ... rm
```

- `k` = cache capacity (`k >= 1`)
- `m` = number of requests
- `r1 ... rm` = sequence of integer request IDs

### Output
Current implementation is menu-driven. After choosing a policy, the program prints:

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

Only the selected policy line is printed for each menu choice.

## How to Run
### Requirements / Build
- Python 3.x
- No external packages required

### Example Commands
Run from the repository root:

```
python src/main.py data/inputs/example.in
```

Then use the menu:
- `1` for FIFO
- `2` for LRU
- `3` for OPTFF
- `4` to exit

## Example Files
- Example input: `data/inputs/example.in`
- Expected output: `data/outputs/example.out`

Input:

```
3 10
1 2 3 1 2 4 1 2 3 4
```

Output:

```
FIFO  : 8
LRU   : 6
OPTFF : 5
```

## Assumptions
- The input file follows the required format: `k m` on the first line and exactly `m` integer requests after it.
- `k >= 1`.
- Request IDs are integers.
- The program keeps showing the menu until option `4` is selected.

## How to Reproduce Outputs
Run:

```
python src/main.py data/inputs/example.in
```

Then choose `1`, `2`, and `3` (in any order) to print each policy result, and choose `4` to exit.
Compare the printed results to `data/outputs/example.out`.

## Written Component
### Question 1: Empirical Comparison

#### Setup
For Question 1, we used three nontrivial input files, each with at least 50 requests:

- `data/inputs/q1_case1.in` (`k = 3`, `m = 60`)
- `data/inputs/q1_case2.in` (`k = 4`, `m = 64`)
- `data/inputs/q1_case3.in` (`k = 5`, `m = 70`)

This section is split 50/50:
- First half (completed here): input design + computed miss counts table.
- Second half (partner): interpretation and comparison commentary.

#### Results
| Input File | k | m | FIFO | LRU | OPTFF |
| --- | --- | --- | --- | --- | --- |
| `q1_case1.in` | 3 | 60 | 56 | 54 | 36 |
| `q1_case2.in` | 4 | 64 | 16 | 16 | 13 |
| `q1_case3.in` | 5 | 70 | 41 | 41 | 27 |

Matching output files:
- `data/outputs/q1_case1.out`
- `data/outputs/q1_case2.out`
- `data/outputs/q1_case3.out`

#### Brief Comment
- Does OPTFF have the fewest misses?
  - Yes, OPTFF has the fewest misses in all three test files. This is expected because OPTFF is the optimal offline cache eviction algorithm.
- How does FIFO compare to LRU?
  - FIFO performed worse than LRU on q1_case1.in, while FIFO and LRU produced the same number of misses on q1_case2.in and q1_case3.in. Thus, LRU was never worse than FIFO in these tests, but it only outperformed FIFO on one of the three request sequences. This result makes sense because LRU keeps recently used items in the cache, which are often needed again soon. FIFO, on the other hand, may remove an item just because it is the oldest one in the cache, even if it will be used again shortly.

### Question 2: Bad Sequence for LRU (k = 3)

#### Claim
There exists a request sequence for cache size `k = 3` on which OPTFF incurs strictly fewer misses than LRU.

This construction follows the cache-eviction comparisons discussed in the course lecture slides [1].

#### Setup
Let:

- Cache size `k = 3`
- Request sequence:

`1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`

#### Computation
Simulating both policies on this fixed sequence gives:

- `LRU` misses: `10`
- `OPTFF` misses: `7`

To see why LRU performs worse, once `4` and `5` appear, LRU repeatedly evicts items that will be needed sooner than the item OPTFF chooses to evict. OPTFF uses future knowledge, so it evicts the page whose next use is farthest in the future and avoids several near-term misses.

#### Conclusion
For this `k = 3` sequence:

`misses(OPTFF) = 7 < 10 = misses(LRU)`

Therefore, a bad sequence for LRU exists where OPTFF incurs strictly fewer misses.

### Question 3: Prove OPTFF is Optimal

#### Theorem: FF produces an optimal eviction schedule.

This proof follows the optimal caching proof presented in the course lecture slides [1].

#### Setup
Fix a request sequence r_1, ..., r_m and cache size k.

Let S_FF be the eviction schedule produced by FF/OPTFF (Belady’s Farthest-in-Future algorithm).

Let A be any offline algorithm, and let S denote the eviction schedule produced by A on this fixed request sequence.

Consider an optimal schedule S (minimum possible misses) that agrees with S_FF for the maximum number of initial steps. Let j be the number of steps for which S and S_FF agree. We will show there exists a schedule S′ that agrees with S_FF for the first j+1 steps and incurs no more misses than S. This contradicts maximality of j, so S must agree with S_FF everywhere, meaning FF/OPTFF is optimal.

#### Proof
Proof by induction on the number of steps j.

The proof follows directly from the following invariant.

#### Invariant
Construct S′ so that:
1. S′ agrees with S_FF through the first j+1 steps.
2. S′ incurs no more misses than S.

Let the (j+1)-st request be to item d. Since S and S_FF agree through the first j steps, they have the same cache contents at this point.

#### Case 1: d is in the cache
No eviction is necessary, so we can set S′ = S.  
Thus S′ = S satisfies the invariant.

#### Case 2: d is not in the cache and S and S_FF evict the same item
Again we set S′ = S.  
Thus S′ = S satisfies the invariant.

#### Case 3: d is not in the cache; S_FF evicts e and S evicts f ≠ e
We begin construction of S′ from S by evicting e instead of f. Now S′ agrees with S_FF for the first j+1 steps. We show that having item f in cache is no worse than having item e in cache.

Let S′ behave the same as S until S′ is forced to take a different action (because either S evicts e, or because either e or f is requested).

Let j′ be the first step after j+1 that S′ must take a different action from S. Let g denote the item requested at step j′.

##### Case 3a: g = e
This cannot happen with FF since there must be a request for f before e, because FF evicted e as the item whose next request occurs farthest in the future.

##### Case 3b: g = f
Item f cannot be in the cache of S. Let e′ be the item that S evicts at this step.

- If e′ = e, then S′ accesses f from cache and now S and S′ have the same cache.
- If e′ ≠ e, we make S′ evict e′ and bring e into the cache. Now S and S′ have the same cache.

We then let S′ behave exactly like S for the remaining requests. As noted in the slides, S′ may no longer be reduced, but it can be transformed into a reduced schedule that still agrees with FF through the first j+1 steps.

##### Case 3c: g ≠ e,f and S evicts e
Make S′ evict f. Now S and S′ have the same cache, and we let S′ behave exactly like S for the remaining requests.

#### Conclusion
In all cases we constructed a schedule S′ that satisfies the invariant: it agrees with S_FF for the first j+1 steps and incurs no more misses than S.

This contradicts the choice of S as an optimal schedule that agreed with S_FF for the maximum number of initial steps. Therefore S must agree with S_FF everywhere, and hence FF/OPTFF is an optimal offline eviction schedule.

Finally, since A was arbitrary and S was the schedule produced by A, we conclude:

misses(OPTFF) ≤ misses(A)

for any offline algorithm A on any fixed request sequence.

## References
[1] COP4533 Lecture Slides, "Chapter-4-2026.pdf" (Greedy Algorithms I).
