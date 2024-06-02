from .Card import Card
from .Suits import Suits
from .Ranks import Ranks
from typing import List
import random

class Deck:
    """
    牌庫
    """
    def __init__(self) -> None:
        self.__cards = self.__generate_cards()
        self.shuffle()

    def draw(self) -> Card:
        """從牌庫頂抽取一張牌

        返回:
            牌庫頂的一張牌

        抛出:
            IndexError: 牌庫沒有牌了
        """
        if len(self.__cards) <= 0:
            raise IndexError("There is no card.")
        return self.__cards.pop()

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def __generate_cards(self) -> List[Card]:
        cards = []
        for suit in Suits:
            for rank in Ranks:
                cards.append(Card(suit, rank))
        return cards
