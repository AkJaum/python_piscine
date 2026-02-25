import sys

"""
This exercise was badly changed during the time i was doing it
Before it was to make a pseudo selling system, together with
value of each item and money, there i wouldn't need argv.
But now they changed it to be another thing and forgotten to
add the split function, i have both pdf if you wanted to see it.
thats the reason to the first tip being strange, since it was for
the previous version and not the actual one
"""


def build_inventory(argv):
    inv = dict()
    for arg in argv:
        parts = arg.split(':', 1)
        name = parts[0]
        if name == '':
            # if argument name is empty, ignore
            continue
        qty = 1
        if len(parts) == 2 and parts[1] != '':
            # basicly if it have name and qty (len(parts == 2))
            # and qty exist (parts[1] != ''), do the "atoi"
            try:
                qty = int(parts[1])
            except ValueError:
                # take the error and ignore invalid argument
                continue
        actual = inv.get(name, 0)
        # get verify if the key already exist, before this parse
        # if it exist before, get that and after sum with, for example
        # another item with the same name, in first ocasion it's 0
        # but if a duplicate comes after, will take the previous one
        # and sum with the new to have only one item with the sum of both
        inv.update({name: actual + qty})
    return inv


def main():
    inventory = build_inventory(sys.argv[1:])
    print("=== Player Inventory System Analysis ===")
    total_sum = 0
    for items_numbers in inventory.values():
        total_sum += items_numbers
    print(f"Total items in inventory: {total_sum}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    for name, qty in inventory.items():
        percent = (qty * 100) / total_sum
        if qty == 1:
            print(f"{name}: {qty} unit ({percent:.1f}%)")
        else:
            print(f"{name}: {qty} units ({percent:.1f}%)")
    most_qty = None
    least_qty = None
    print("\n=== Inventory Statistics ===")
    for name, qty in inventory.items():
        if most_qty is None:
            most_qty = qty
            most_name = name
        elif most_qty < qty:
            most_qty = qty
            most_name = name
        if least_qty is None:
            least_name = name
            least_qty = qty
        elif least_qty > qty:
            least_qty = qty
            least_name = name
    if most_qty == 1:
        print(f"Most abundant: {most_name} ({most_qty} unit)")
    else:
        print(f"Most abundant: {most_name} ({most_qty} units)")
    if least_qty == 1:
        print(f"Least abundant: {least_name} ({least_qty} unit)")
    else:
        print(f"Least abundant: {least_name} ({least_qty} units)")
    # organizing
    moderate = dict()
    scarce = dict()
    restock = dict()
    # organizing
    for name, qty in inventory.items():
        if qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})
        if qty == 1:
            restock.update({name: qty})
    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {list(restock.keys())}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print("Sample lookup - 'sword' in "
          "inventory:", inventory.get('sword', 0) > 0)


if __name__ == '__main__':
    main()
