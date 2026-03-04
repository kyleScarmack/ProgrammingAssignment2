import sys

from fifo import run_fifo
from lru import run_lru
from optff import run_optff


def read_input(path):
    # Read cache size and request sequence from file
    with open(path) as f:
        tokens = f.read().split()

    k = int(tokens[0])  # Cache capacity (k >= 1)
    m = int(tokens[1])  # Number of requests
    reqs = list(map(int, tokens[2:]))   # Sequence of integer IDs

    return k, reqs


def print_menu():
    print("\nCache Policy Menu")
    print("1. FIFO")
    print("2. LRU")
    print("3. OPTFF")
    print("4. Exit")


def main():
    if len(sys.argv) != 2:
        print("Input: python3 main.py <inputfile>")
        return

    k, reqs = read_input(sys.argv[1])

    while True:
        print_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print(f"FIFO  : {run_fifo(k, reqs)}")
        elif choice == "2":
            print(f"LRU   : {run_lru(k, reqs)}")
        elif choice == "3":
            print(f"OPTFF : {run_optff(k, reqs)}")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
