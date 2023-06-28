from dataclasses import dataclass

@dataclass
class Quest:
    name: str
    description: str
    reward: int
