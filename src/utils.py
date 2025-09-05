from pathlib import Path

terminal_symbols = ["#", "*", "_", "-", "\n"]


def read_markdown(input_path: str) -> str:
    with Path.open(input_path, encoding="utf-8") as f:
        return f.read()


def write_html(html: str, output_path: str) -> None:
    with Path.open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
