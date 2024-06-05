from node import Node


class WhileOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        conditional = self.children[0].evaluate(symble_table)
        block = self.children[1].evaluate(symble_table)

        while conditional and block is not None:
            block
