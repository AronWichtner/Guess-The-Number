from dataclasses import dataclass


@dataclass
class UserLevelInput:
    level: int = None
    limits: [int] = None
    is_valid: bool = False
