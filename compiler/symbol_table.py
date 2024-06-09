class SymbolTable:
    def __init__(self):
        self.symbol = {}
        self.day_time = 24 * 60

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

    def consume_day_time(self, key, value):

        self.day_time -= value
        if self.day_time < 0:
            raise TypeError("Time is up!")

    def consume_token_time(self, key, value):
        if key in self.symbol:
            self.symbol[key] -= value
            if self.symbol[key] < 0:
                raise TypeError("Time is up!")
        else:
            raise TypeError("Var not declared !")

    def reset_day_time(self):
        self.day_time = 24 * 60
        self.symbol = {}
        print("="*50)

    def check_var_exists(self, key):
        return key in self.symbol
