import alchemy.potions
from elements import create_fire


def lead_to_gold() -> str:
    return (
            f"Recipe transmuting Lead to Gold: brew '{alchemy.create_air()}' "
            f"and '{alchemy.strength_potion()}' mixed with '{create_fire()}'"
        )
