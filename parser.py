from tokens import TokenType
from ast_nodes import NumberNode, VarNode, BinOpNode, AssignNode, PrintNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self):
        """Move to the next token safely."""
        if self.pos < len(self.tokens):
            self.pos += 1

    def current_token(self):
        """Return the current token or None if at the end."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    # def parse(self):
    #     """Parse the tokenized input and construct an AST."""
    #     nodes = []
    #     while self.current_token() is not None:
    #         node = self.statement()
    #         if node:
    #             nodes.append(node)
    #         else:
    #             # If no valid statement, move to next token to avoid infinite loop
    #             self.consume()
    #     return nodes

    # In the Parser's parse() method:
    def parse(self):
        """Parse the tokenized input and construct an AST."""
        nodes = []
        while self.current_token() is not None:
            node = self.statement()
            if node:
                if isinstance(node, list):
                    nodes.extend(node)  # Flatten lists
                else:
                    nodes.append(node)  # Append single nodes
            else:
                self.consume()
        return nodes

    def statement(self):
        """Parse a single statement."""
        token = self.current_token()
        if token is None:
            return None

        if token.type == TokenType.LET:
            return self.assignment()
        elif token.type == TokenType.PRINT:
            return self.print_statement()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def assignment(self):
        """Parse assignment statements like 'let x = 10;' and 'let a = 10, b = 20;'"""
        self.consume()  # Consume 'let'
        assignments = []

        while True:
            if self.current_token().type != TokenType.ID:
                raise SyntaxError("Expected variable name in assignment")

            var_name = self.current_token().value
            self.consume()  # Consume variable name

            if self.current_token().type != TokenType.ASSIGN:
                raise SyntaxError("Expected '=' in assignment")

            self.consume()  # Consume '='
            expr = self.expression()  # Parse the expression

            assignments.append(AssignNode(var_name, expr))

            # Handle multiple assignments (comma-separated)
            if self.current_token().type == TokenType.COMMA:
                self.consume()  # Consume ','
                continue  # Continue parsing next assignment

            # Ensure assignment ends with a semicolon
            elif self.current_token().type == TokenType.SEMICOLON:
                self.consume()  # Consume ';'
                return assignments

            else:
                raise SyntaxError("Expected ';' at the end of the assignment statement")


    def print_statement(self):
        """Parse a print statement: print x;"""
        self.consume()  # Consume 'print'
        expr = self.expression()

        if self.current_token() and self.current_token().type == TokenType.SEMICOLON:
            self.consume()  # Consume ';'
        else:
            raise SyntaxError("Expected ';' at the end of the print statement")

        return PrintNode(expr=expr)

    def expression(self):
        """Parse addition and subtraction expressions."""
        left = self.term()  # Start with a term (handles multiplication, division, and parentheses)

        while self.current_token() and self.current_token().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token().type
            self.consume()
            right = self.term()
            left = BinOpNode(left, op, right)  # Construct a binary operation node

        return left

    def term(self):
        """Parse multiplication and division expressions."""
        left = self.factor()  # Start with a factor (numbers, variables, parentheses)

        while self.current_token() and self.current_token().type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token().type
            self.consume()
            right = self.factor()
            left = BinOpNode(left, op, right)  # Construct a binary operation node

        return left

    def factor(self):
        """Parse numbers, variables, or parenthesized expressions."""
        token = self.current_token()
        if token is None:
            raise SyntaxError("Unexpected end of input while parsing")

        if token.type == TokenType.NUMBER:
            self.consume()
            return NumberNode(token.value)

        elif token.type == TokenType.ID:
            self.consume()
            return VarNode(token.value)

        elif token.type == TokenType.LPAREN:  # Handle (expr)
            self.consume()  # Consume '('
            expr = self.expression()  # Parse the inside expression

            if self.current_token() and self.current_token().type == TokenType.RPAREN:
                self.consume()  # Consume ')'
                return expr
            else:
                raise SyntaxError("Expected ')' after expression")

        else:
            raise SyntaxError(f"Unexpected token: {token}")