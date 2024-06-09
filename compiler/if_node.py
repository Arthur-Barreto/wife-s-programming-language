from node import Node


class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        cond_node_ret = self.children[0].evaluate(symble_table)
        conditional = cond_node_ret[0]
        task_name = cond_node_ret[1]
        time_if_block = self.children[1].evaluate(symble_table)

        task_time = symble_table.get_identifier(task_name)

        if conditional:

            print("*" * 50)

            symble_table.consume_day_time(task_name, time_if_block)
            symble_table.consume_token_time(task_name, time_if_block)
            task_time -= time_if_block
            if task_time > 0:
                print(f"{task_name} ainda tem {task_time} min")
            else:
                print(f"O tempo acabou para {task_name} !")

            print(f"Você ainda tem {symble_table.day_time} min para este dia !")
            print("*" * 50)
            
        else:
            raise Exception(f"Error: {task_name} mal planejada !")
