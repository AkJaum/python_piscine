import functools
import operator
from typing import Callable, Dict


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells is None or len(spells) == 0:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError("Invalid operation")


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def spell_dispatcher(spell):
    return "Unknown spell type"


@spell_dispatcher.register
def _(spell: int):
    return f"Damage spell: {spell} damage"


@spell_dispatcher.register
def _(spell: str):
    return f"Enchantment: {spell.lower()}"


@spell_dispatcher.register
def _(spell: list):
    return f"Multi-cast: {len(spell)} spells"


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(spell_reducer([1, 2, 3], "add"))
    print(spell_reducer([2, 2, 3], "multiply"))
    print(spell_reducer([1, 2, 3], "max"))
    print(spell_reducer([1, 2, 3], "min"))

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Enchants {target} with {element} ({power} power)"

    partial_enchant = partial_enchanter(base_enchantment)
    print(partial_enchant["fire"]("Sword"))
    print(partial_enchant["ice"]("Shield"))
    print(partial_enchant["lightning"]("Axe"))

    print("\nTesting memoized Fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("Fireball"))
    print(spell_dispatcher(["Ice Shard", "Lightning Bolt"]))
    print(spell_dispatcher(3.14))
