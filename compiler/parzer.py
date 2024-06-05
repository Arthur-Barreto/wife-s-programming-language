from tokenizer import Tokenizer
from bin_op import BinOp
from un_op import UnOp
from int_val import IntVal
from no_op import NoOp
from assignment import Assignment
from identifier import Identifier
from print_node import Print
from block import Block
from while_node import WhileOp
from if_node import IfOp
from read_val import ReadVal
from str_val import StrVal
from var_dec import VarDec
from return_node import ReturnNode


class Parser:
    tokenizer = None

    @staticmethod
    def parse_block():

        # block = Block(children=[])

        # while Parser.tokenizer.next.type != "EOF":
        #     line = Parser.parse_statement()
        #     block.children.append(line)

        # return block
        # teste the tokenizer to validade until get the EOF
        while Parser.tokenizer.next.type != "EOF":
            Parser.tokenizer.select_next()

    @staticmethod
    def parse_statement():

        if Parser.tokenizer.next.type == "NEWLINE":
            Parser.tokenizer.select_next()
            return NoOp()

        elif Parser.tokenizer.next.type == "IDENTIFIER":
            variable = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "ASSIGN":
                Parser.tokenizer.select_next()
                res = Parser.bool_expression()
                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError(
                        "Missing newline after empty line on 'identifier'"
                    )
                Parser.tokenizer.select_next()
                return Assignment(value=None, children=[variable, res])
            else:
                raise SyntaxError(
                    "Missing newline or varaible assigment after identifier !"
                )

        elif Parser.tokenizer.next.type == "LOCAL":

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "IDENTIFIER":
                raise SyntaxError("Expected variable declaration after 'local' !")

            variable = Parser.tokenizer.next.value

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "NEWLINE":
                Parser.tokenizer.select_next()
                return VarDec(value=None, children=[variable])

            elif Parser.tokenizer.next.type == "ASSIGN":
                Parser.tokenizer.select_next()
                res = Parser.bool_expression()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after empty line on 'local'")

                Parser.tokenizer.select_next()

                return VarDec(value=None, children=[variable, res])

            else:
                raise SyntaxError("Missing newline or varaible assigment after local !")

        elif Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise SyntaxError("Missing '('")

            Parser.tokenizer.select_next()
            res = Parser.bool_expression()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'print'")

            Parser.tokenizer.select_next()
            return Print(children=[res])

        elif Parser.tokenizer.next.type == "WHILE":
            Parser.tokenizer.select_next()
            while_conditional = Parser.bool_expression()

            if Parser.tokenizer.next.type != "DO":
                raise SyntaxError("Missing 'do'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'do'")

            Parser.tokenizer.select_next()

            while_block = Block(children=[])
            while Parser.tokenizer.next.type != "END":
                line = Parser.parse_statement()
                while_block.children.append(line)

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'end' from 'while'")

            Parser.tokenizer.select_next()
            return WhileOp(
                value=None,
                children=[while_conditional, while_block],
            )

        elif Parser.tokenizer.next.type == "IF":
            Parser.tokenizer.select_next()
            if_conditional = Parser.bool_expression()

            if Parser.tokenizer.next.type != "THEN":
                raise SyntaxError("Missing 'then' after 'if'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing nweline after 'then' from 'if'")

            Parser.tokenizer.select_next()

            if_block = Block(children=[])
            else_block = Block(children=[])
            while Parser.tokenizer.next.type not in ["ELSE", "END"]:
                line = Parser.parse_statement()
                if_block.children.append(line)

            if Parser.tokenizer.next.type == "END":
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'end' from 'if'")

                Parser.tokenizer.select_next()
                return IfOp(
                    value=None,
                    children=[if_conditional, if_block, else_block],
                )

            elif Parser.tokenizer.next.type == "ELSE":
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'else'")

                Parser.tokenizer.select_next()

                while Parser.tokenizer.next.type != "END":
                    line = Parser.parse_statement()
                    else_block.children.append(line)

                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'end' from 'else'")

                Parser.tokenizer.select_next()
                return IfOp(
                    value=None,
                    children=[if_conditional, if_block, else_block],
                )
            else:
                raise SyntaxError("Missing 'end' or 'else' after 'if'")

        elif Parser.tokenizer.next.type == "FUNCTION":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "IDENTIFIER":
                raise SyntaxError("Missing function name after 'function'")

            identifier_node = Identifier(value=Parser.tokenizer.next.value)
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise SyntaxError("Missing '(' after function name")

            Parser.tokenizer.select_next()

            func_dec_child = [identifier_node]

            if Parser.tokenizer.next.type == "IDENTIFIER":
                var_dec = VarDec(value=None, children=[Parser.tokenizer.next.value])
                func_dec_child.append(var_dec)
                Parser.tokenizer.select_next()

                while Parser.tokenizer.next.type == "COMMA":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type != "IDENTIFIER":
                        raise SyntaxError("Missing argument after ','")

                    var_dec = VarDec(value=None, children=[Parser.tokenizer.next.value])
                    func_dec_child.append(var_dec)
                    Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')' after function arguments")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError(
                    f"Missing newline after function declaration, got= {Parser.tokenizer.next.type}"
                )

            Parser.tokenizer.select_next()

            func_block = Block(children=[])

            while Parser.tokenizer.next.type != "END":
                line = Parser.parse_statement()
                func_block.children.append(line)

            func_dec_child.append(func_block)

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'end' from function")

            Parser.tokenizer.select_next()

            return FuncDec(value=None, children=func_dec_child)

        elif Parser.tokenizer.next.type == "RETURN":
            Parser.tokenizer.select_next()
            res = Parser.bool_expression()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'return'")

            Parser.tokenizer.select_next()
            return ReturnNode(children=[res])

        else:
            raise SyntaxError("Invalid Input")

    @staticmethod
    def bool_expression():
        result = Parser.bool_term()

        while Parser.tokenizer.next.type == "OR":
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.bool_term()],
            )

        return result

    @staticmethod
    def bool_term():
        result = Parser.relational_expression()

        while Parser.tokenizer.next.type == "AND":
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.relational_expression()],
            )

        return result

    @staticmethod
    def relational_expression():
        result = Parser.parse_expression()

        while Parser.tokenizer.next.type in ["EQ", "LT", "GT"]:
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_expression()],
            )

        return result

    @staticmethod
    def parse_expression():
        result = Parser.parse_term()

        while Parser.tokenizer.next.type in ["PLUS", "MINUS", "DOUBLE_DOT"]:
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_term()],
            )

        return result

    @staticmethod
    def parse_term():
        result = Parser.parse_factor()

        while Parser.tokenizer.next.value in ["*", "/"]:
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_factor()],
            )

        return result

    @staticmethod
    def parse_factor():

        if Parser.tokenizer.next.type == "INT":
            result = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return IntVal(value=result)

        elif Parser.tokenizer.next.type in ["STRING"]:
            result = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return StrVal(value=result)

        elif Parser.tokenizer.next.type == "IDENTIFIER":
            name = Parser.tokenizer.next.value

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "LPAREN":
                Parser.tokenizer.select_next()
                args = []
                if Parser.tokenizer.next.type == "RPAREN":
                    Parser.tokenizer.select_next()
                    return FuncCall(value=name, children=args)
                res = Parser.bool_expression()
                args.append(res)
                while Parser.tokenizer.next.type == "COMMA":
                    Parser.tokenizer.select_next()
                    res = Parser.bool_expression()
                    args.append(res)
                if Parser.tokenizer.next.type != "RPAREN":
                    raise SyntaxError("Missing ')' after function arguments")
                Parser.tokenizer.select_next()
                return FuncCall(value=name, children=args)

            return Identifier(value=name)

        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.select_next()
            return UnOp(
                value="+",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.select_next()
            return UnOp(
                value="-",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.select_next()
            return UnOp(
                value="not",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "LPAREN":
            Parser.tokenizer.select_next()
            result = Parser.bool_expression()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')'")
            Parser.tokenizer.select_next()
            return result

        elif Parser.tokenizer.next.type == "READ":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise SyntaxError("Missing '(' after 'read'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')' after 'read'")

            Parser.tokenizer.select_next()

            return ReadVal()

        else:
            print(f"{Parser.tokenizer.next.type} | {Parser.tokenizer.next.value}")
            raise SyntaxError("Invalid Input")

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_block()
