from ex0.factories import AquaFactory, FlameFactory
from ex1.factories import HealingFactory, TransformFactory
from ex2.strategies import (
    InvalidStrategyCreatureError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def run_battle(left, right) -> None:
    left_factory, left_strategy = left
    right_factory, right_strategy = right
    left_creature = left_factory.create_base()
    right_creature = right_factory.create_base()
    print("\n* Battle *")
    print(left_creature.describe())
    print(" vs.")
    print(right_creature.describe())
    print(" now fight!")

    for action in left_strategy.act(left_creature):
        print(action)
    for action in right_strategy.act(right_creature):
        print(action)


def tournament(opponents: list[tuple]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for left_index in range(len(opponents)):
        for right_index in range(left_index + 1, len(opponents)):
            try:
                run_battle(opponents[left_index], opponents[right_index])
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
