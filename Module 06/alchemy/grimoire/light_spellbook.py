def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    for item in result.split(" "):
        if "INVALID" in item:
            return (
                f"Spell '{spell_name}' failed to record"
            )
    return f"Spell recorded: {spell_name} ({result})"
