from alchemy.grimoire.dark_spellbook import dark_spell_record

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    spell_result = dark_spell_record(
        "Forbidden spell",
        "bats and frogs",
    )
    print(
        f"Testing dark spell record: "
        f"{spell_result}"
    )
