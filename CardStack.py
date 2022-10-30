from __future__ import annotations

import random
import copy
from typing import Union, Iterable, List


class CardStack:
    values: List[int]

    def __init__(self, val: Union[int, Iterable[int], None] = None):

        if val is None:
            self.values = []

        elif type(val) is int:
            values = []
            for i in range(val):
                values.append(int(random.randrange(-100, 100)))
            self.values = values

        elif hasattr(val, '__iter__'):
            self.values = [int(i) for i in val]

    def shuffled(self) -> CardStack:
        values = copy.copy(self.values)
        random.shuffle(values)
        return CardStack(values)

    def combine(self, other: CardStack) -> CardStack:
        biggestList = len(self.values) if len(self.values) > len(other.values) else len(other.values)
        values = []
        for i in range(biggestList):
            if len(self.values) > i:
                values.append(self.values[i])
            if len(other.values) > i:
                values.append(other.values[i])
        return CardStack(values)

    def add(self, value: int) -> None:
        #self.values.insert(0, value)
        self.values.append(value)

    def __len__(self) -> int:
        return len(self.values)

card1 = CardStack((1,2,3))
print(card1.values)
card2 = card1.shuffled()
print(card1.values)
print(card2.values)
card2 = CardStack((4,5,6,7))
card3 = card1.combine(card2)
print(card2.values)
print(card3.values)
print(card2.values)

card3.add(99)

print(card3.values)
print(len(card3))