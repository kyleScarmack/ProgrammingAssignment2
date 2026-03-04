# Programming Assignment 2 - Greedy Algorithms

## Overview
Programming Assignment 2 implements and compares three cache eviction policies: FIFO (First-In, First-Out), LRU (Least Recently Used), and OPTFF (Belady's Farthest-in-Future, optimal offline), on the same sequence of cache requests. The program reads a cache capacity and request stream from an input file, simulates each policy, and outputs the number of cache misses for each one. The assignment also (1) empirically compares miss counts across multiple nontrivial inputs, (2) constructs and analyzes a bad request sequence for FIFO or LRU when k = 3, and (3) proves that OPTFF is optimal among offline algorithms, meaning it never produces more misses than any other offline strategy on the same request sequence.

## Students
- Student 1: Brock Gilman - UFID: 58803474
- Student 2: Kyle Scarmack - UFID: 20823723

## Repository Structure
- `src/main.py` - Program entry point. Reads input file and runs implemented policies.
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
Current implementation output format:

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## How to Run
### Requirements / Build
- Python 3.x
- No external packages required

### Example Commands
Run from the repository root:

```
python src/main.py data/inputs/example.in
```

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
TODO

## How to Reproduce Outputs
Run:

```
python src/main.py data/inputs/example.in
```

Compare your terminal output to `data/outputs/example.out`.

## Written Component
### Question 1
TODO

### Question 2
TODO

### Question 3
TODO
