from parzer import Parser
from pre_pro import PrePro
from symbol_table import SymbolTable
import sys


if __name__ == "__main__":

    file_name = sys.argv[1]
    wife_code = PrePro.filter(file_name)
    s_table = SymbolTable()
    tree = Parser.run(wife_code)

    if Parser.tokenizer.next.type != "EOF":
        raise SyntaxError("Should have an operator! ")

    result = tree.evaluate(symble_table=s_table)
    
    # print all variables in the symbol table
    # for key, value in s_table.symbol.items():
    #     print(f"{key} = {value}")
        
    print(f"total de minutos restantes {s_table.day_time}")

    # if result != None:
    #     print(result)
