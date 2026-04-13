from abc import ABC, abstractmethod


class InvalidStrategyCreatureError(Exception):
    """Raised when a strategy is used with an invalid Creature."""


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
        return [creature.attack()]

    def is_valid(self, creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
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

    def is_valid(self, creature) -> bool:
        return (
            hasattr(creature, "transform")
            and hasattr(creature, "attack")
            and hasattr(creature, "revert")
        )


# Backward-compatible alias for typo present in older code.
AgressiveStrategy = AggressiveStrategy


class DefensiveStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
        if self.is_valid(creature):
            return [creature.attack(), creature.heal()]
        raise InvalidStrategyCreatureError(
            "Invalid Creature "
            f"'{creature.name}' for this defensive strategy"
        )

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "attack") and hasattr(creature, "heal")
