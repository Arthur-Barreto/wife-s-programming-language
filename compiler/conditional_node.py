from node import Node


class ConditionalNode(Node):
    def __init__(self, value):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        str_val = self.value
        time_left = symble_table.get_identifier(str_val)
        return (time_left > 0, str_val)
