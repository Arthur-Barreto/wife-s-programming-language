from node import Node


class Block(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        for line in self.children:
            node = line.evaluate(symble_table)

            if type(line).__name__ == "ReturnNode":
                return node

