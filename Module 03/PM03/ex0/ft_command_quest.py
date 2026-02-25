import sys


def main():
    print("=== Command Quest ===\n")
    if (len(sys.argv) == 1):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}\n")
    elif (len(sys.argv) > 1):
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}\n")


main()
