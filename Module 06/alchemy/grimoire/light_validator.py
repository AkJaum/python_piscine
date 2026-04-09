_LIGHT_ALLOWED_INGREDIENTS = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    allowed = 0
    for ingredient in ingredients.split(","):
        if ingredient.strip() not in _LIGHT_ALLOWED_INGREDIENTS:
            pass
        else:
            allowed += 1
    if allowed > 0:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
