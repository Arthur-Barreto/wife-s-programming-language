from node import Node


class Print(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        print(self.children[0].evaluate(symble_table)[0])
