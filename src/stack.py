from src.abstract_syntax_tree import Node


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: Node) -> None:
        self.items.append(item)

    def pop(self) -> Node or None:
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> Node or None:
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.items) == 0
