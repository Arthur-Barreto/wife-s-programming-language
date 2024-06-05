from node import Node


class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        n1 = self.children[0].evaluate(symble_table)
        n2 = self.children[1].evaluate(symble_table)

        if type(n1) == bool:
            if n1:
                n1 = (1, "INT")
            else:
                n1 = (0, "INT")

        if type(n2) == bool:
            if n2:
                n2 = (1, "INT")
            else:
                n2 = (0, "INT")

        if n1[1] == n2[1] and (self.value in ["EQ", "LT", "GT"]):
            if self.value == "EQ":
                if n1[0] == n2[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

            elif self.value == "LT":
                if n1[0] < n2[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

            elif self.value == "GT":
                if n1[0] > n2[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

        elif (
            (n1[1] == "INT")
            and (n2[1] == "INT")
            and (self.value in ["PLUS", "MINUS", "MULT", "DIV", "AND", "OR"])
        ):
            if self.value == "PLUS":
                return (n1[0] + n2[0], "INT")
            elif self.value == "MINUS":
                return (n1[0] - n2[0], "INT")
            elif self.value == "MULT":
                return (n1[0] * n2[0], "INT")
            elif self.value == "DIV":
                return (n1[0] // n2[0], "INT")
            elif self.value == "AND":
                bool_value = n1[0] and n2[0]
                if bool_value:
                    return (1, "INT")
                else:
                    return (0, "INT")
            elif self.value == "OR":
                bool_value = n1[0] or n2[0]
                if bool_value:
                    return (1, "INT")
                else:
                    return (0, "INT")

        elif self.value == "DOUBLE_DOT":
            return (str(n1[0]) + str(n2[0]), "STRING")

        else:
            print(f"op= {self.value}")
            raise TypeError("Unknow operation !")
