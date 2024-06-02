from .Suits import Suits
from .Ranks import Ranks

class Card:
    """
    撲克牌
    """
    def __init__(self, suit: Suits, rank: Ranks) -> None:
        self.suit = suit
        self.rank = rank
    def __repr__(self) -> str:
        return self.suit.value + self.rank.value