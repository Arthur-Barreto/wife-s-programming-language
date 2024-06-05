from node import Node


class Identifier(Node):
    def __init__(self, value):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        try:
            return symble_table.get_identifier(key=self.value)
        except Exception as e:
            raise TypeError("Undefined variable: " + self.value)
