from node import Node


class ActionNode(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        str_val = self.value
        action_time = self.children[0]
        print(f"Ela fez '{str_val}' por {action_time} min !")

