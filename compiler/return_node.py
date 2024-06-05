from node import Node


class ReturnNode(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        return self.children[0].evaluate(symble_table)
