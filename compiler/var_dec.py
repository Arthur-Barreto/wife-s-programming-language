from node import Node


class VarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        if len(self.children) == 2:
            symble_table.create_identifier(
                key=self.children[0], value=self.children[1].evaluate(symble_table)
            )
        else:
            symble_table.create_identifier(key=self.children[0], value=None)
