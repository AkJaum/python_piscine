from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heals {target} {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} and dealt {power} damage"


def lightning_strike(target: str, power: int) -> str:
    return f"Lightning strikes {target} with {power} volts"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> str:
        result1 = spell1(target, power).split(target)[0].strip()
        result2 = spell2(target, power).split(target)[0].strip()
        return f"{result1} {target}, {result2} {target}"

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        base_spell(target, power * multiplier)
        return f"Original: {power}, Amplified: {power * multiplier}"

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> str:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return "\n".join(results)

    return sequence_spell


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    print(f"combined spell result: {combined('Orc', 50)}")

    amplified_heal = power_amplifier(heal, 2)
    print(f"\nAmplified spell result: {amplified_heal('Elf', 30)}")

    def is_mob(target: str, power: int) -> bool:
        return target == "Vampire"

    night_spell = conditional_caster(is_mob, fireball)
    print(
        f"\nConditional spell result (Vampire): {night_spell('Vampire', 40)}"
    )
    print(f"Conditional spell result (Human): {night_spell('Human', 40)}")

    sequence = spell_sequence([heal, fireball, lightning_strike])
    print(f"\nSpell sequence result: \n{sequence('Dragon', 60)}")
