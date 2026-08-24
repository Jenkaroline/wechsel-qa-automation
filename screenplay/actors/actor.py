from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Type, TypeVar


AbilityType = TypeVar("AbilityType")


@dataclass
class Actor:
    name: str
    _abilities: Dict[type, Any] = field(default_factory=dict)

    def can(self, *abilities: Any) -> "Actor":
        for ability in abilities:
            self._abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_type: Type[AbilityType]) -> AbilityType:
        if ability_type not in self._abilities:
            raise KeyError(f"Actor {self.name} does not have ability {ability_type.__name__}")
        return self._abilities[ability_type]

    def attempts_to(self, *tasks: Any) -> "Actor":
        for task in tasks:
            task.perform_as(self)
        return self

    def asks_for(self, question: Any) -> Any:
        return question.answered_by(self)
