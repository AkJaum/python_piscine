from .dark_validator import validate_ingredients


dark_spell_allowed_ingredients = ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    for item in result.split(" "):
        if "INVALID" in item:
            raise ValueError(
                f"Spell '{spell_name}' failed to record due to "
                f"invalid ingredient: {item.split(':')[0]}"
            )
    return result
