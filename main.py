from pathlib import Path

from src import utils
from src.converter import ast_to_html
from src.lexer import Lexer
from src.parser import Parser

file_name = "test"
INPUT_PATH = Path("examples") / f"{file_name}.md"
OUTPUT_PATH = Path("examples") / f"{file_name}.html"

markdown = utils.read_markdown(INPUT_PATH)

lexer = Lexer(markdown)
tokens = lexer.tokenize()

parser = Parser(tokens)
ast = parser.parse()

html = ast_to_html(ast)

utils.write_html(html, OUTPUT_PATH)
