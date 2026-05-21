def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    most_powerful = max(mages, key=lambda x: x['power'])
    least_powerful = min(mages, key=lambda x: x['power'])
    average_power = sum(mage['power'] for mage in mages) / len(mages)
    return {
        "max_power": most_powerful,
        "min_power": least_powerful,
        "avg_power": average_power
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Grass Sword", "power": 50},
        {"name": "Cloak of Invisibility", "power": 70}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    mages = [
        {"name": "Gandalf", "power": 100},
        {"name": "Dumbledore", "power": 150},
        {"name": "Saruman", "power": 120},
        {"name": "Radagast", "power": 30}
    ]
    filtered_mages = power_filter(mages, 100)
    print(
        "Mages with power >= 100: "
        + ', '.join(mage['name'] for mage in filtered_mages)
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "lightning", "ice shard"]
    transformed_spells = spell_transformer(spells)
    print(f"{' '.join(transformed_spells)}")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Most powerful mage: {stats['max_power']['name']} "
        f"with {stats['max_power']['power']} power"
    )
    print(
        f"Least powerful mage: {stats['min_power']['name']} "
        f"with {stats['min_power']['power']} power"
    )
    print(f"Average power: {stats['avg_power']}")
