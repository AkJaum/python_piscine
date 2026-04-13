from ex0 import CreatureFactory, AquaFactory, FlameFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def demo_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    flame_creature = factory1.create_base()
    aqua_creature = factory2.create_base()
    print(flame_creature.describe())
    print("vs.")
    print(aqua_creature.describe())

    print("fight!")
    print(flame_creature.attack())
    print(aqua_creature.attack())


if __name__ == "__main__":
    testing_factory(FlameFactory())
    print()
    testing_factory(AquaFactory())
    print()
    demo_battle(FlameFactory(), AquaFactory())
