from node import Node


class WhileOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        cond_node_ret = self.children[0].evaluate(symble_table)
        conditional = cond_node_ret[0]
        task_name = cond_node_ret[1]
        while_block_time = self.children[1].evaluate(symble_table)

        task_time = symble_table.get_identifier(task_name)

        if conditional:

            while task_time > 0 and task_time >= while_block_time:
                print(f"{task_name} ainda tem {task_time} min")
                symble_table.consume_token_time(task_name, while_block_time)
                symble_table.consume_day_time(task_name, while_block_time)
                task_time -= while_block_time
                
            if task_time > 0:
                print(f"{task_name} ainda tem {task_time} min")
            else:
                print(f"O tempo acabou para {task_name} !")
                
            print(f"Você ainda tem {symble_table.day_time} min para este dia !")

        else:
            raise Exception(f"Error: {task_name} mal planejada !")
