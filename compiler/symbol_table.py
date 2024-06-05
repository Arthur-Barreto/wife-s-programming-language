class SymbolTable:
    def __init__(self):
        self.symbol = {}

    def create_identifier(self, key, value=None):
        if key in self.symbol:
            raise TypeError("Var already declared !")
        self.symbol[key] = value

    def set_identifier(self, key, value=None):

        if key not in self.symbol:
            raise TypeError("You must declare the variable first !")

        if type(value) in [int, bool]:
            self.symbol[key] = (int(value), "INT")
        elif type(value) == str:
            self.symbol[key] = (value, "STRING")
        elif type(value) == tuple:
            if value[1] == "INT":
                self.symbol[key] = (value[0], "INT")
            elif value[1] == "STRING":
                self.symbol[key] = (value[0], "STRING")
        elif value is None:
            self.symbol[key] = (None, None)
        else:
            print(f"type= {type(value)}")
            raise TypeError("Invalid type atribution!")

    def get_identifier(self, key):
        if key in self.symbol:
            return self.symbol[key]
        raise TypeError("Var not declared !")

    def check_var_exists(self, key):
        return key in self.symbol
