from .Card import Card
from typing import List

class Board:
    """
    共牌
    """
    def __init__(self)-> None:
        self.__maximum_cards = 5
        self.__cards = []
    
    def add_card_to_board(self, card: Card) -> None:
        """將牌加入到共牌

        抛出:
            OverflowError: 已達共牌上限
        """
        if len(self.__cards) == self.__maximum_cards:
            raise OverflowError("Too many cards.")
        self.__cards.append(card)

    def cards(self) -> List[Card]:
        return self.__cards