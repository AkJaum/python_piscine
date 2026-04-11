from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    output_str = ""
    for ingredient in ingredients.split(","):
        if ingredient.strip() not in dark_spell_allowed_ingredients:
            output_str += f"{ingredient.strip()}:INVALID "
        else:
            output_str += f"{ingredient.strip()}:VALID "

    return output_str
