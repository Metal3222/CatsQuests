from __future__ import annotations

from collections.abc import Iterable, Iterator

class stack_chain:

    def __init__(self, *iterables: Iterable):
        pass

    def __iter__(self) -> Iterator:
        pass

    def __iadd__(self, iterable: Iterable) -> stack_chain:
        pass
