from node import Node


class Block(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        time_spent = 0
        for token in self.children:
            time = token.evaluate(symble_table)
            if time is not None:
                time_spent += time
                
        print(f"block time {time_spent}")
        
        return time_spent
            