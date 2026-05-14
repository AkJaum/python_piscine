from typing import Tuple, List
from ex0.factories import AquaFactory, FlameFactory
from ex1.factories import HealingFactory, TransformFactory
from ex2.strategies import (
    InvalidStrategyCreatureError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def run_battle(creature_1: Tuple, creature_2: Tuple) -> None:
    c1_factory, c1_strategy = creature_1
    c2_factory, c2_strategy = creature_2
    c1_creature = c1_factory.create_base()
    c2_creature = c2_factory.create_base()
    print("\n* Battle *")
    print(c1_creature.describe())
    print(" vs.")
    print(c2_creature.describe())
    print(" now fight!")

    for action in c1_strategy.act(c1_creature):
        print(action)
    for action in c2_strategy.act(c2_creature):
        print(action)


def tournament(opponents: List[Tuple]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for creature_1 in range(len(opponents) - 1):
        for creature_2 in range(creature_1 + 1, len(opponents)):
            try:
                run_battle(opponents[creature_1], opponents[creature_2])
            except InvalidStrategyCreatureError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_0 = [
        (FlameFactory(), normal),
        (HealingFactory(), defensive),
    ]
    tournament(opponents_0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_1 = [
        (FlameFactory(), aggressive),
        (HealingFactory(), defensive),
    ]
    tournament(opponents_1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_2 = [
        (AquaFactory(), normal),
        (HealingFactory(), defensive),
        (TransformFactory(), aggressive),
    ]
    tournament(opponents_2)
