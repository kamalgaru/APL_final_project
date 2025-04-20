from tokens import TokenType

class Token:
    def __init__(self, type_, value=None):
        """Represents a token with a type and an optional value."""
        self.type = type_
        self.value = value

    def __repr__(self):
        """Provides a readable string representation of a token for debugging."""
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        """Initializes the lexer with the input text and starting position."""
        self.text = text
        self.pos = 0

    def advance(self):
        """Moves the lexer’s current position forward by one character."""
        self.pos += 1

    def peek(self):
        """Looks ahead one character without moving the current position."""
        if self.pos + 1 < len(self.text):
            return self.text[self.pos + 1]
        return ''

    def get_next_token(self):
        """Scans the input text and returns the next token found.

        Handles different token types:
        - Whitespace skipping
        - Comments
        - Keywords
        - Identifiers (variable names)
        - Numbers (integers and decimals)
        - Strings
        - Multi-character operators
        - Single-character tokens
        - Raises error for illegal characters
        """
        if self.pos >= len(self.text):
            return Token(TokenType.EOF)

        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return Token(TokenType.EOF)

        current_char = self.text[self.pos]

        # Handle Comments
        if current_char == '#':
            start = self.pos
            while self.pos < len(self.text) and self.text[self.pos] != '\n':
                self.pos += 1
            return Token(TokenType.COMMENT, self.text[start:self.pos])

        # Handle Keywords
        keywords = {
            "let": TokenType.LET, "print": TokenType.PRINT, "return": TokenType.RETURN,
            "if": TokenType.IF, "else": TokenType.ELSE, "elif": TokenType.ELIF,
            "for": TokenType.FOR, "while": TokenType.WHILE, "function": TokenType.FUNCTION,
            "class": TokenType.CLASS, "import": TokenType.IMPORT, "from": TokenType.FROM,
            "as": TokenType.AS, "try": TokenType.TRY, "except": TokenType.EXCEPT,
            "finally": TokenType.FINALLY, "break": TokenType.BREAK, "continue": TokenType.CONTINUE,
            "pass": TokenType.PASS, "def": TokenType.DEF, "global": TokenType.GLOBAL,
            "nonlocal": TokenType.NONLOCAL, "raise": TokenType.RAISE, "assert": TokenType.ASSERT,
            "in": TokenType.IN, "is": TokenType.IS, "lambda": TokenType.LAMBDA,
            "match": TokenType.MATCH, "case": TokenType.CASE,
            "and": TokenType.AND, "or": TokenType.OR, "not": TokenType.NOT
        }

        for keyword, token_type in keywords.items():
            if self.text.startswith(keyword, self.pos) and \
               (self.pos + len(keyword) == len(self.text) or not self.text[self.pos + len(keyword)].isalnum()):
                self.pos += len(keyword)
                return Token(token_type)

        # Identifiers (variable names)
        if current_char.isalpha() or current_char == '_':
            start = self.pos
            while self.pos < len(self.text) and (self.text[self.pos].isalnum() or self.text[self.pos] == '_'):
                self.pos += 1
            return Token(TokenType.ID, self.text[start:self.pos])

        # Numbers (integers and floats)
        # if current_char.isdigit():
        #     start = self.pos
        #     while self.pos < len(self.text) and self.text[self.pos].isdigit():
        #         self.pos += 1
        #     if self.pos < len(self.text) and self.text[self.pos] == '.':
        #         self.pos += 1
        #         while self.pos < len(self.text) and self.text[self.pos].isdigit():
        #             self.pos += 1
        #     return Token(TokenType.NUMBER, self.text[start:self.pos])

        # Inside the Lexer's get_next_token() method (number handling section):
        if current_char.isdigit():
            start = self.pos
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.pos += 1
            if self.pos < len(self.text) and self.text[self.pos] == '.':
                self.pos += 1
                while self.pos < len(self.text) and self.text[self.pos].isdigit():
                    self.pos += 1
            num_str = self.text[start:self.pos]
            # Convert to int or float
            if '.' in num_str:
                value = float(num_str)
            else:
                value = int(num_str)
            return Token(TokenType.NUMBER, value)  # Now stores int/float instead of str

        # String literals
        if current_char in ('"', "'"):
            quote = current_char
            self.pos += 1
            start = self.pos
            while self.pos < len(self.text) and self.text[self.pos] != quote:
                if self.text[self.pos] == '\\' and self.pos + 1 < len(self.text):
                    self.pos += 2
                else:
                    self.pos += 1
            string_value = self.text[start:self.pos]
            self.pos += 1
            return Token(TokenType.STRING, string_value)

        # Multi-character operators (like ==, !=, **)
        multi_char_ops = {
            '==': TokenType.EQUALS, '!=': TokenType.NOT_EQUALS, '<=': TokenType.LESS_EQUAL,
            '>=': TokenType.GREATER_EQUAL, '**': TokenType.POWER, '//': TokenType.FLOOR_DIV,
            '+=': TokenType.PLUS_ASSIGN, '-=': TokenType.MINUS_ASSIGN, '*=': TokenType.MUL_ASSIGN,
            '/=': TokenType.DIV_ASSIGN, '%=': TokenType.MOD_ASSIGN, '**=': TokenType.POWER_ASSIGN,
            '//=': TokenType.FLOOR_DIV_ASSIGN, '->': TokenType.ARROW, '=>': TokenType.DOUBLE_ARROW,
            '<<': TokenType.BIT_LSHIFT, '>>': TokenType.BIT_RSHIFT
        }

        for op, token_type in sorted(multi_char_ops.items(), key=lambda x: -len(x[0])):
            if self.text.startswith(op, self.pos):
                self.pos += len(op)
                return Token(token_type)

        # Single-character tokens (+, -, *, /, etc.)
        single_char_map = {
            '+': TokenType.PLUS, '-': TokenType.MINUS, '*': TokenType.MUL, '/': TokenType.DIV,
            '%': TokenType.MODULO, '=': TokenType.ASSIGN, '<': TokenType.LESS_THAN,
            '>': TokenType.GREATER_THAN, '(': TokenType.LPAREN, ')': TokenType.RPAREN,
            '{': TokenType.LBRACE, '}': TokenType.RBRACE, '[': TokenType.LBRACKET, ']': TokenType.RBRACKET,
            ',': TokenType.COMMA, '.': TokenType.DOT, ':': TokenType.COLON, ';': TokenType.SEMICOLON,
            '&': TokenType.BIT_AND, '|': TokenType.BIT_OR, '^': TokenType.BIT_XOR, '~': TokenType.BIT_NOT,
            '?': TokenType.QUESTION_MARK, '!': TokenType.EXCLAMATION_MARK
        }

        if current_char in single_char_map:
            self.pos += 1
            return Token(single_char_map[current_char])

        # If no valid token found, raise an error
        raise SyntaxError(f"Illegal character: {current_char}")

    def tokenize(self):
        """Splits the entire input text into a list of token lists, one list per line.

        - Processes the input line by line.
        - Calls get_next_token repeatedly for each line.
        - Collects all non-EOF tokens for each line.
        """
        tokenized_output = []
        lines = self.text.split("\n")

        for line in lines:
            self.pos = 0
            self.text = line
            line_tokens = []
            while self.pos < len(self.text):
                token = self.get_next_token()
                if token.type == TokenType.EOF:
                    break
                line_tokens.append(token)
            tokenized_output.append(line_tokens)

        return tokenized_output
