from src.abstract_syntax_tree import (
    Bold,
    Document,
    Italic,
    List,
    Node,
    Paragraph,
    Text,
    Title,
)
from src.lexer import Token
from src.stack import Stack


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.token_parsers = {
            "HEADER": self.parse_header,
            "LIST_ITEM": self.parse_list_item,
            "TEXT": self.parse_inline,
            "BOLD": self.parse_inline,
            "ITALIC": self.parse_inline,
            "NEW_LINE": self.parse_new_line,
        }

    def parse(self) -> Document:
        document = Document()
        stack = Stack()
        stack.push(document)

        for idx, token in enumerate(self.tokens):
            parse = self.token_parsers.get(token.type)
            if not parse:
                raise ParserError(f"Token inválido na posição {idx}: {token.type}")
            parse(token, stack)

        # ✅ Verifica se restaram estilos abertos
        while not stack.is_empty():
            top = stack.pop()
            if isinstance(top, (Bold, Italic)):
                raise ParserError(f"Nó {top.__class__.__name__} não foi fechado.")

        return document

    def managet_list_exit(self, token: Token, stack: Stack) -> None:
        top = stack.peek()
        if isinstance(top, List) and token.type not in ["LIST_ITEM", "NEW_LINE"]:
            stack.pop()

    def parse_header(self, token: Token, stack: Stack) -> None:
        current_node = stack.peek()
        title = Title(level=len(token.value), text="")
        current_node.children.append(title)
        stack.push(title)

    def parse_list_item(self, _: Token, stack: Stack) -> None:
        top = stack.peek()
        if not isinstance(top, List):
            lst = List()
            top.children.append(lst)
            stack.push(lst)

        current_list = stack.peek()
        item = Paragraph()
        current_list.items.append(item)
        stack.push(item)

    def parse_inline(self, token: Token, stack: Stack) -> None:
        top = stack.peek()
        if isinstance(top, Document):
            paragraph = Paragraph()
            top.children.append(paragraph)
            stack.push(paragraph)

        current_node = stack.peek()

        if token.type == "TEXT":
            current_node.children.append(Text(token.value))
        elif token.type == "BOLD":
            self.parse_style(stack, Bold)
        elif token.type == "ITALIC":
            self.parse_style(stack, Italic)

    def parse_style(self, stack: Stack, node_class: Node) -> None:
        current_node = stack.peek()
        if isinstance(current_node, node_class):
            stack.pop()
        else:
            style_node = node_class()
            current_node.children.append(style_node)
            stack.push(style_node)

    def parse_new_line(self, _: Token, stack: Stack) -> None:
        while not stack.is_empty() and isinstance(stack.peek(), (Title, Paragraph)):
            stack.pop()
