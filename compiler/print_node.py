from node import Node


class Print(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        task = self.children[0].evaluate(symble_table)
        time = self.children[1].evaluate(symble_table)
        # print(f"{task} {time}")
        return time
