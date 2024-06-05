from node import Node


class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        conditional = self.children[0].evaluate(symble_table)
        if_block = self.children[1].evaluate(symble_table)
        else_block = self.children[2].evaluate(symble_table)

        if conditional:
            if_block

        else:
            else_block
