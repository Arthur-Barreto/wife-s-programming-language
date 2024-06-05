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

        self.symbol[key] = value

    def get_identifier(self, key):
        if key in self.symbol:
            return self.symbol[key]
        raise TypeError("Var not declared !")

    def check_var_exists(self, key):
        return key in self.symbol
