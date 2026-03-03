import sys

from fifo import run_fifo


def read_input(path):
    # Read cache size and request sequence from file
    with open(path) as f:
        tokens = f.read().split()

    k = int(tokens[0])  # Cache capacity (k >= 1)
    m = int(tokens[1])  # Number of requests
    reqs = list(map(int, tokens[2:]))   # Sequence of integer IDs

    return k, reqs


def main():
    if len(sys.argv) != 2:
        print("Input: python3 main.py <inputfile>")
        return

    k, reqs = read_input(sys.argv[1])

    fifo = run_fifo(k, reqs)

    print(f"FIFO  : {fifo}")


if __name__ == "__main__":
    main()