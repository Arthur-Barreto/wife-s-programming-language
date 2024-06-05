from node import Node


class ReadVal(Node):
    def __init__(self):
        super().__init__(None, [])

    def evaluate(self, symbol_table):
        return (int(input()), "INT")
