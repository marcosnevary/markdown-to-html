class Node:
    def __init__(self) -> None:
        self.children = []


class Document(Node):
    def __init__(self) -> None:
        super().__init__()


class Title(Node):
    def __init__(self, level: int, text: str) -> None:
        super().__init__()
        self.level = level
        self.text = text


class Paragraph(Node):
    def __init__(self) -> None:
        super().__init__()


class List(Node):
    def __init__(self) -> None:
        super().__init__()
        self.items = []


class Text(Node):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value


class Bold(Node):
    def __init__(self) -> None:
        super().__init__()


class Italic(Node):
    def __init__(self) -> None:
        super().__init__()
