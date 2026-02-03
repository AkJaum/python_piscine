def ft_seed_inventory(seed: str, quantity: int, seed_type: str) -> None:
    if seed_type == "packets":
        print(f"{seed.capitalize()} seeds: {quantity} packets available")
    elif seed_type == "grams":
        print(f"{seed.capitalize()} seeds: {quantity} grams total")
    elif seed_type == "area":
        print(f"{seed.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
