from src.utils import terminal_symbols


class Token:
    def __init__(self, token_type: str, token_value: str) -> None:
        self.type = token_type
        self.value = token_value


class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0

    def current(self) -> None or str:
        return self.text[self.pos] if self.pos < len(self.text) else None

    def advance(self, steps: int = 1) -> None:
        self.pos += steps

    def peek(self, steps: int = 1) -> None or str:
        pos = self.pos + steps
        return self.text[pos] if pos < len(self.text) else None

    def tokenize_header(self) -> Token:
        count = 0

        while self.current() == "#":
            count += 1
            self.advance()

        if self.current() == " ":
            self.advance()

        return Token("HEADER", "#" * count)

    def tokenize_bold(self) -> Token:
        self.advance(2)
        return Token("BOLD", "**")

    def tokenize_italic(self) -> Token:
        self.advance()
        return Token("ITALIC", "_")

    def tokenize_list_item(self) -> Token:
        self.advance()

        if self.current() == " ":
            self.advance()

        return Token("LIST_ITEM", "-")

    def tokenize_new_line(self) -> Token:
        self.advance()
        return Token("NEW_LINE", "\\n")

    def tokenize_text(self) -> Token:
        text = ""

        while self.current() is not None and self.current() not in terminal_symbols:
            text += self.current()
            self.advance()

        return Token("TEXT", text)

    def tokenize(self) -> list:
        tokens = []

        while self.current() is not None:
            char = self.current()

            if char == "#":
                tokens.append(self.tokenize_header())

            elif char == "*" and self.peek() == "*":
                tokens.append(self.tokenize_bold())

            elif char == "_":
                tokens.append(self.tokenize_italic())

            elif char == "-" and (self.pos == 0 or self.text[self.pos - 1] == "\n"):
                tokens.append(self.tokenize_list_item())

            elif char == "\n":
                tokens.append(self.tokenize_new_line())

            else:
                text_token = self.tokenize_text()
                if text_token.value:
                    tokens.append(text_token)

        return tokens
