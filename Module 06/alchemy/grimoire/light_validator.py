from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = [
        i.lower() for i in light_spell_allowed_ingredients()
    ]
    allowed = 0
    for ingredient in ingredients.split(","):
        if ingredient.strip().lower() in allowed_ingredients:
            allowed += 1
    if allowed > 0:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
