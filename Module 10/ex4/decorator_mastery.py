from functools import wraps
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in: {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, target: str, power: int) -> str:
            if power < min_power:
                return "Insufficient power for this spell."
            return func(self, target, power)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts - 1:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... (attempt "
                        f"{attempts + 1}/{max_attempts})"
                    )
                    attempts += 1
            print(f"Spell casting failed after {max_attempts} attempts")
            return "Waaaaaaagh spelled !"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return name.isalpha() and len(name) > 3

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if not self.validate_mage_name(spell_name):
            return "Invalid spell name"
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.734)  # Simulate casting time
        return f"Fireball hits {target} with {power} power"

    print(fireball("Orc", 50))

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise ValueError("Spell failed!")

    print(unstable_spell())

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print("True: " + mage_guild.cast_spell("Fireball", 15))
    print("False: " + mage_guild.cast_spell("Ice Spike", 5))
