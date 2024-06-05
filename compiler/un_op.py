from node import Node


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        n1 = self.children[0].evaluate(symble_table)

        if type(n1) == bool:
            if n1:
                n1 = (1, "INT")
            else:
                n1 = (0, "INT")

        if n1[1] != "INT":
            raise SyntaxError("Wrong type, should be 'int' for 'unop' !")

        if self.value == "-":
            return (-n1[0], "INT")
        elif self.value == "+":
            return (n1[0], "INT")
        elif self.value == "not":
            return not (n1[0], "INT")
