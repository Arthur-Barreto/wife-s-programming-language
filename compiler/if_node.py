from node import Node


class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        cond_node_ret = self.children[0].evaluate(symble_table)
        conditional = cond_node_ret[0]
        task_name = cond_node_ret[1]
        time_if_block = self.children[1].evaluate(symble_table)
        
        if conditional:
            print(f"{task_name} realizada, gastando {time_if_block} minutos")
            symble_table.consume_day_time(task_name, time_if_block)
            print(f"total de minutos restantes {symble_table.day_time}")
            symble_table.consume_token_time(task_name, time_if_block)
        else:
            raise Exception(f"Error: {task_name} mal planejada !")
