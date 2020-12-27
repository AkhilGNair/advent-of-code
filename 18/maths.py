from pathlib import Path
import ast
from astor import to_source


MAP = str.maketrans("+*", "*+")
OPS = {ast.Add: ast.Mult(), ast.Mult: ast.Add()}


def calc(text):
    tree = ast.parse(text.translate(MAP))
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            node.op = OPS[type(node.op)]
    return eval(to_source(tree))


equations = Path("input.txt").read_text().split("\n")
print(sum(map(calc, equations)))
