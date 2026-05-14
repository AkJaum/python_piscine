from abc import ABC, abstractmethod
from ._creatures import Creature


class InvalidStrategyCreatureError(Exception):
    """Raised when a strategy is used with an invalid Creature."""


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            return [
                creature.transform(),
                creature.attack(),
                creature.revert(),
            ]
        raise InvalidStrategyCreatureError(
            "Invalid Creature "
            f"'{creature.name}' for this aggressive strategy"
        )

    def is_valid(self, creature: Creature) -> bool:
        return (
            hasattr(creature, "transform")
            and hasattr(creature, "attack")
            and hasattr(creature, "revert")
        )


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            return [creature.attack(), creature.heal()]
        raise InvalidStrategyCreatureError(
            "Invalid Creature "
            f"'{creature.name}' for this defensive strategy"
        )

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack") and hasattr(creature, "heal")
