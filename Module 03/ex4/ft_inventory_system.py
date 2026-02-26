import sys


def current_inventory(inventory: dict, total_items: int) -> None:
    print("\n=== Current Inventory ===")
    printed = 0
    total_unique = len(inventory)
    used = {}
    while printed < total_unique:
        max_value = -1
        max_key = ""
        for name, value in inventory.items():
            if name not in used and value > max_value:
                max_value = value
                max_key = name
        if max_value > 1:
            print(
                f"{max_key}: {max_value} units "
                f"({((max_value / total_items) * 100):.1f}%)"
            )
        else:
            print(
                f"{max_key}: {max_value} unit "
                f"({((max_value / total_items) * 100):.1f}%)"
            )
        used[max_key] = True
        printed += 1


def inv_stats(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    first = True
    for name, value in inventory.items():
        if first:
            max_name = name
            max_value = value
            min_name = name
            min_value = value
            first = False
        else:
            if value > max_value:
                max_value = value
                max_name = name
            if value < min_value:
                min_value = value
                min_name = name
    print(f"Most abundant: {max_name} ({max_value} units)")
    print(f"Least abundant: {min_name} ({min_value} unit)")


def init_inv(inventory: dict) -> int:
    total_items = 0
    unique_items = 0
    if not sys.argv[1:]:
        print("No arguments provided!")
        return 0
    for arg in sys.argv[1:]:
        name, value = arg.split(":")
        value = int(value)
        inventory[name] = inventory.get(name, 0) + value
    for value in inventory.values():
        total_items += value
        unique_items += 1
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    return total_items


def item_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    restock = []
    for name, value in inventory.items():
        if value >= 5:
            moderate[name] = value
        if value < 5:
            scarce[name] = value
        if value == 1:
            restock.append(name)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    print(*restock, sep=", ")


def dict_demos(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    print(*inventory.keys(), sep=", ")
    print("Dictionary values:", end=" ")
    print(*inventory.values(), sep=", ")
    if inventory.get("sword") is None:
        print("Sample lookup - 'sword' in inventory: False")
    else:
        print("Sample lookup - 'sword' in inventory: True")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    total_items = init_inv(inventory)
    if total_items == 0:
        print("No items to analyze.")
        sys.exit(0)
    current_inventory(inventory, total_items)
    inv_stats(inventory)
    item_categories(inventory)
    dict_demos(inventory)
