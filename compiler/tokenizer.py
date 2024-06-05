import re


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = Token(type=None, value="")

        self.reserved_variables = {
            "HORA_DE_BRILHAR": "HORA_DE_BRILHAR",
            "SEMPRE_DIVA": "SEMPRE_DIVA",
            "GRUNIDO": "GRUNIDO",
            "A_MIMIR": "A_MIMIR",
            "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA": "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA",
            "SE": "SE",
            "TAREFA": "TAREFA",
            "HABLAR": "HABLAR",
            "ACAO": "ACAO",
            "TO_COM_FOME": "TO_COM_FOME",
            "QUERO_PITDAS": "QUERO_PITDAS",
        }

        if len(self.source.strip()) == 0:
            raise TypeError("Empty Input")

    def select_next(self):

        while self.position < len(self.source):
            char = self.source[self.position]

            if char == " " or char == "\t":
                self.position += 1

            elif char == ".":
                self.next.type = "DOT"
                self.next.value = "."
                self.position += 1
                return

            elif (
                char == "<"
                and self.position + 1 < len(self.source)
                and self.source[self.position + 1] == "<"
            ):

                self.next.type = "TAREFA_DECLARATION"
                self.next.value = "<<"
                self.position += 2
                return

            elif (
                char == ">"
                and self.position + 1 < len(self.source)
                and self.source[self.position + 1] == ">"
            ):
                self.next.type = "ACAO_DECLARATION"
                self.next.value = ">>"
                self.position += 2
                return

            elif char == "(":
                self.next.type = "LPAREN"
                self.next.value = "("
                self.position += 1
                return

            elif char == ")":
                self.next.type = "RPAREN"
                self.next.value = ")"
                self.position += 1
                return

            elif char == ",":
                self.next.type = "COMMA"
                self.next.value = ","
                self.position += 1
                return

            elif char == "\n":
                self.next.type = "NEWLINE"
                self.next.value = None
                self.position += 1
                return

            elif re.match(r"[a-zA-Z_]", char):
                self.next.value = char
                self.position += 1
                while self.position < len(self.source) and re.match(
                    r"\w", self.source[self.position]
                ):
                    self.next.value += self.source[self.position]
                    self.position += 1

                if self.next.value in self.reserved_variables:
                    self.next.type = self.reserved_variables[self.next.value]
                    return

                self.next.type = "IDENTIFIER"
                return

            elif char.isdigit():
                self.next.type = "INT"
                self.next.value = char
                self.position += 1
                while (
                    self.position < len(self.source)
                    and self.source[self.position].isdigit()
                ):
                    self.next.value += self.source[self.position]
                    self.position += 1
                self.next.value = int(self.next.value)
                return

            else:
                raise TypeError(f"invalid char: '{char}' NOT ALLOWED !")

        self.next.type = "EOF"
        self.next.value = ""
