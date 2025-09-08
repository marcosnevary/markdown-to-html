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


def ast_to_html(node: Node) -> str:
    html = ""

    if isinstance(node, Text):
        html = node.value

    elif isinstance(node, Document):
        html = ""

        for child in node.children:
            html += ast_to_html(child) + "\n"

        html = html.rstrip()

    elif isinstance(node, Paragraph):
        html = wrap_children(node, "p")

    elif isinstance(node, Title):
        html = wrap_children(node, f"h{node.level}")

    elif isinstance(node, Bold):
        html = wrap_children(node, "strong")

    elif isinstance(node, Italic):
        html = wrap_children(node, "em")

    elif isinstance(node, List):
        html = "<ul>"

        for item in node.items:
            html += f"<li>{ast_to_html(item)}</li>"

        html += "</ul>"

    return html


def wrap_children(node: Node, tag: str) -> str:
    html = f"<{tag}>"

    for child in node.children:
        html += ast_to_html(child)

    html += f"</{tag}>"

    return html
