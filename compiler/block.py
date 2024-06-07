from node import Node


class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        time_spent = 0
        for token in self.children:
            time = token.evaluate(symble_table)
            if time is not None:
                time_spent += time
                
        if self.value == "PAI":
            # symble_table.reset_day_time()
            pass
            
        elif self.value != "PITDAS":
            # print("hablar ....... fora de PITDAS")
            pass
        
        return time_spent
            