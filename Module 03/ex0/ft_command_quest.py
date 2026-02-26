import sys


if __name__ == "__main__":
    i = 1
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print("Program name:", sys.argv[0])
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print("Total arguments", len(sys.argv))
