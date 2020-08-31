from dataclasses import dataclass


@dataclass
class Level:
    level: int = None
    limits: [int] = None
    user_lives: [str] = None
    is_valid: bool = False

    def reduce_live(self):
        del self.user_lives[-1]
