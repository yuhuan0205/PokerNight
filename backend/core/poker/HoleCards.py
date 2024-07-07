from .Card import Card
from typing import List

class HoleCards:
    """
    底牌
    """
    def __init__(self) -> None:
        self.__maximum_cards = 2
        self.__cards = []

    def show_hole_cards(self) -> List[Card]:
        """展示底牌

        返回:
            所有底牌
        """
        return self.__cards
    
    def add_card_to_hole_cards(self, card: Card) -> None:
        """新增一張牌至底牌中

        抛出:
            OverflowError: 已達底牌上限
        """
        if len(self.__cards) == self.__maximum_cards:
            raise OverflowError("Too many cards.")
        self.__cards.append(card)