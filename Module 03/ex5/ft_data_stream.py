from typing import Generator
import time


def generate_events(n: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie", "david"]
    actions = ["killed monster", "found treasure", "leveled up", "leveled up"]

    for i in range(n):
        name = players[i % len(players)]
        level = (i % 14) + 1
        action = actions[i % len(actions)]

        event = f"Event {i + 1}: Player {name} (level {level}) {action}"
        yield event


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    start_time = time.time()
    for event in generate_events(1000):
        print(event)
        total += 1
        if "(level " in event:
            level = int(event.split("(level ")[1].split(")")[0])
            if level >= 10:
                high_level += 1
        if "found treasure" in event:
            treasure += 1
        if "leveled up" in event:
            level_up += 1
    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        if i <= 8:
            print(next(fib), end=", ")
        else:
            print(next(fib), end="")

    prime_gen = primes()
    print("\nPrime numbers (first 5): ", end="")
    for i in range(5):
        if i <= 3:
            print(next(prime_gen), end=", ")
        else:
            print(next(prime_gen), end="")


if __name__ == "__main__":
    main()
