from tokenizer import Tokenizer
from bin_op import BinOp
from int_val import IntVal
from no_op import NoOp
from assignment import Assignment
from identifier import Identifier
from print_node import Print
from block import Block
from while_node import WhileOp
from if_node import IfOp
from str_val import StrVal
from var_dec import VarDec  


class Parser:
    tokenizer = None

    @staticmethod
    def parse_block():

        if Parser.tokenizer.next.type != "HORA_DE_BRILHAR":
            raise SyntaxError(
                "Expected 'HORA_DE_BRILHAR' at the beginning of the block"
            )

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'HORA_DE_BRILHAR'")

        Parser.tokenizer.select_next()

        block = Block(children=Parser.parse_days())

        if Parser.tokenizer.next.type != "SEMPRE_DIVA":
            raise SyntaxError("Expected 'SEMPRE_DIVA' at the end of the block")

        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'SEMPRE_DIVA'")

        Parser.tokenizer.select_next()

        return block

    @staticmethod
    def parse_days():
        days = []
        while Parser.tokenizer.next.type == "GRUNIDO":
            days.append(Parser.parse_day())
        return days

    @staticmethod
    def parse_day():
        if Parser.tokenizer.next.type != "GRUNIDO":
            raise SyntaxError("Expected 'GRUNIDO' at the beginning of the day")

        Parser.tokenizer.select_next()


        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'GRUNIDO'")

        Parser.tokenizer.select_next()


        statements = Parser.parse_statements()

        if Parser.tokenizer.next.type != "A_MIMIR":
            raise SyntaxError("Expected 'A_MIMIR' at the end of the day")

        Parser.tokenizer.select_next()


        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'A_MIMIR'")

        Parser.tokenizer.select_next()


        return Block(children=statements)

    @staticmethod
    def parse_statements():
        statements = []
        while Parser.tokenizer.next.type not in ["A_MIMIR", "SEMPRE_DIVA", "BLOCK_END"]:
            statements.append(Parser.parse_statement())
        return statements

    @staticmethod
    def parse_statement():
        if Parser.tokenizer.next.type == "NEWLINE":
            Parser.tokenizer.select_next()

            return NoOp()

        elif Parser.tokenizer.next.type == "TAREFA":
            return Parser.parse_task_declaration()

        elif Parser.tokenizer.next.type == "ACAO":
            return Parser.parse_action_declaration()

        elif Parser.tokenizer.next.type == "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA":
            return Parser.parse_while_statement()

        elif Parser.tokenizer.next.type == "SE":
            return Parser.parse_if_statement()

        elif Parser.tokenizer.next.type == "HABLAR":
            return Parser.parse_hablar_statement()

        elif Parser.tokenizer.next.type == "BLOCK_BEGIN":
            return Parser.parse_block_statements()

        else:
            raise SyntaxError(f"Invalid statement {Parser.tokenizer.next.type}")

    @staticmethod
    def parse_task_declaration():
        if Parser.tokenizer.next.type != "TAREFA":
            raise SyntaxError(
                "Expected 'TAREFA' at the beginning of the task declaration"
            )

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "TAREFA_DECLARATION":
            raise SyntaxError("Expected task declaration")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "LPAREN":
            raise SyntaxError("Expected '(' after task declaration")

        Parser.tokenizer.select_next()
        string_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()


        if Parser.tokenizer.next.type != "COMMA":
            raise SyntaxError("Expected ',' after string value")

        Parser.tokenizer.select_next()
        number_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()


        if Parser.tokenizer.next.type != "RPAREN":
            raise SyntaxError("Expected ')' after number value")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after task declaration")

        Parser.tokenizer.select_next()
        return VarDec(value="TAREFA", children=[string_val, number_val])

    @staticmethod
    def parse_action_declaration():
        if Parser.tokenizer.next.type != "ACAO":
            raise SyntaxError(
                "Expected 'ACAO' at the beginning of the action declaration"
            )

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "ACAO_DECLARATION":
            raise SyntaxError("Expected action declaration")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "LPAREN":
            raise SyntaxError("Expected '(' after action declaration")

        Parser.tokenizer.select_next()
        string_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type != "COMMA":
            raise SyntaxError("Expected ',' after string value")

        Parser.tokenizer.select_next()
        number_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type != "RPAREN":
            raise SyntaxError("Expected ')' after number value")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after action declaration")

        Parser.tokenizer.select_next()
        return VarDec(value="ACAO", children=[string_val, number_val])

    @staticmethod
    def parse_while_statement():
        if Parser.tokenizer.next.type != "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA":
            raise SyntaxError(
                "Expected 'ENQUANTO_ELA_NAO_MUDA_DE_IDEIA' at the beginning of the while statement"
            )

        Parser.tokenizer.select_next()
        condition = Parser.parse_conditional()

        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after condition")

        Parser.tokenizer.select_next()
        block_statements = Parser.parse_block_statements()
        return WhileOp(value="ENQUANTO", children=[condition, block_statements])

    @staticmethod
    def parse_if_statement():
        if Parser.tokenizer.next.type != "SE":
            raise SyntaxError("Expected 'SE' at the beginning of the if statement")

        Parser.tokenizer.select_next()
        condition = Parser.parse_conditional()

        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after condition")

        Parser.tokenizer.select_next()
        block_statements = Parser.parse_block_statements()
        return IfOp(value="SE", children=[condition, block_statements])

    @staticmethod
    def parse_hablar_statement():
        if Parser.tokenizer.next.type != "HABLAR":
            raise SyntaxError(
                "Expected 'HABLAR' at the beginning of the hablar statement"
            )

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "LPAREN":
            raise SyntaxError("Expected '(' after 'HABLAR'")

        Parser.tokenizer.select_next()
        string_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type != "COMMA":
            raise SyntaxError("Expected ',' after string value")

        Parser.tokenizer.select_next()
        number_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type != "RPAREN":
            raise SyntaxError("Expected ')' after number value")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'HABLAR'")

        Parser.tokenizer.select_next()
        return Print(children=[StrVal(value=string_val), IntVal(value=number_val)])

    @staticmethod
    def parse_conditional():
        if Parser.tokenizer.next.type != "TAREFA":
            raise SyntaxError("Expected 'TAREFA' at the beginning of the conditional")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "DOT":
            raise SyntaxError("Expected '.' in the conditional")

        Parser.tokenizer.select_next()
        string_val = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()
        return BinOp(
            value="CONDICIONAL",
            children=[Identifier(value="TAREFA"), StrVal(value=string_val)],
        )

    @staticmethod
    def parse_block_statements():
        if Parser.tokenizer.next.type != "BLOCK_BEGIN":
            raise SyntaxError(
                "Expected 'BLOCK_BEGIN' at the beginning of block statements"
            )

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'BLOCK_BEGIN'")

        Parser.tokenizer.select_next()
        statements = Parser.parse_statements()

        if Parser.tokenizer.next.type != "BLOCK_END":
            raise SyntaxError("Expected 'BLOCK_END' at the end of block statements")

        Parser.tokenizer.select_next()
        if Parser.tokenizer.next.type != "NEWLINE":
            raise SyntaxError("Expected newline after 'BLOCK_END'")

        Parser.tokenizer.select_next()
        return Block(children=statements)

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_block()
