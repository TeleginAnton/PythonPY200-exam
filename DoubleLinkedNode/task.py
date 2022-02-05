from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):

        self.value = value

        self.next_ = None
        self.set_next(next_)

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next_ = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next_ is None else f"Node({self.value}, Node({self.next_}))"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"] = None) -> None:
        self.is_valid(prev)
        self._prev = None if prev is None else prev

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next_ is None else f"DoubleLinkedNode({self.next_})"

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"


if __name__ == "__main__":
    test = Node(50)
    test2 = Node(3, test)
    print(repr(test2))

    test3 = DoubleLinkedNode(100)
    test4 = DoubleLinkedNode(100, test3)
    print(repr(test4))
