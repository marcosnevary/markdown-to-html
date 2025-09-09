from pathlib import Path

from src import utils
from src.converter import ast_to_html
from src.lexer import Lexer
from src.parser import Parser


def markdown_to_html(file_name: str) -> None:
    input_path = Path("input") / f"{file_name}.md"
    output_path = Path("output") / f"{file_name}.html"

    markdown = utils.read_markdown(input_path)

    lexer = Lexer(markdown)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    html = ast_to_html(ast)

    utils.write_html(html, output_path)


file_names = ["example_1", "example_2", "example_3", "article_example"]

for file_name in file_names:
    markdown_to_html(file_name)
