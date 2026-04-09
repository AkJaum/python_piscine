_DARK_ALLOWED_INGREDIENTS = ["bats", "frogs", "arsenic", "eyeball"]


def validate_ingredients(ingredients: str) -> str:
    output_str = ""
    for ingredient in ingredients.split(","):
        if ingredient.strip() not in _DARK_ALLOWED_INGREDIENTS:
            output_str += f"{ingredient.strip()}:INVALID "
        else:
            output_str += f"{ingredient.strip()}:VALID "

    return output_str
