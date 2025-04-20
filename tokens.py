class TokenType:
    # Keywords
    LET = "LET"
    PRINT = "PRINT"
    RETURN = "RETURN"
    IF = "IF"
    ELSE = "ELSE"
    ELIF = "ELIF"
    FOR = "FOR"
    WHILE = "WHILE"
    FUNCTION = "FUNCTION"
    CLASS = "CLASS"
    IMPORT = "IMPORT"
    FROM = "FROM"
    AS = "AS"
    TRY = "TRY"
    EXCEPT = "EXCEPT"
    FINALLY = "FINALLY"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    PASS = "PASS"
    DEF = "DEF"
    GLOBAL = "GLOBAL"
    NONLOCAL = "NONLOCAL"
    RAISE = "RAISE"
    ASSERT = "ASSERT"
    IN = "IN"
    IS = "IS"
    LAMBDA = "LAMBDA"
    MATCH = "MATCH"
    CASE = "CASE"

    # Identifiers & Literals
    ID = "ID"
    NUMBER = "NUMBER"
    STRING = "STRING"
    CHAR = "CHAR"

    # Operators
    PLUS = "PLUS"            # +
    MINUS = "MINUS"          # -
    MUL = "MUL"              # *
    DIV = "DIV"              # /
    MODULO = "MODULO"        # %
    POWER = "POWER"          # **
    FLOOR_DIV = "FLOOR_DIV"  # //
    
    # Comparison Operators
    EQUALS = "EQUALS"        # ==
    NOT_EQUALS = "NOT_EQUALS"  # !=
    LESS_THAN = "LESS_THAN"  # <
    LESS_EQUAL = "LESS_EQUAL"  # <=
    GREATER_THAN = "GREATER_THAN"  # >
    GREATER_EQUAL = "GREATER_EQUAL"  # >=

    # Assignment Operators
    ASSIGN = "ASSIGN"  # =
    PLUS_ASSIGN = "PLUS_ASSIGN"  # +=
    MINUS_ASSIGN = "MINUS_ASSIGN"  # -=
    MUL_ASSIGN = "MUL_ASSIGN"  # *=
    DIV_ASSIGN = "DIV_ASSIGN"  # /=
    MOD_ASSIGN = "MOD_ASSIGN"  # %=
    POWER_ASSIGN = "POWER_ASSIGN"  # **=
    FLOOR_DIV_ASSIGN = "FLOOR_DIV_ASSIGN"  # //=

    # Logical Operators
    AND = "AND"  # and
    OR = "OR"  # or
    NOT = "NOT"  # not

    # Bitwise Operators
    BIT_AND = "BIT_AND"  # &
    BIT_OR = "BIT_OR"  # |
    BIT_XOR = "BIT_XOR"  # ^
    BIT_NOT = "BIT_NOT"  # ~
    BIT_LSHIFT = "BIT_LSHIFT"  # <<
    BIT_RSHIFT = "BIT_RSHIFT"  # >>

    # Delimiters & Separators
    LPAREN = "LPAREN"  # (
    RPAREN = "RPAREN"  # )
    LBRACE = "LBRACE"  # {
    RBRACE = "RBRACE"  # }
    LBRACKET = "LBRACKET"  # [
    RBRACKET = "RBRACKET"  # ]
    COMMA = "COMMA"  # ,
    DOT = "DOT"  # .
    COLON = "COLON"  # :
    SEMICOLON = "SEMICOLON"  # ;
    ARROW = "ARROW"  # ->
    DOUBLE_ARROW = "DOUBLE_ARROW"  # =>
    QUESTION_MARK = "QUESTION_MARK"  # ?
    EXCLAMATION_MARK = "EXCLAMATION_MARK"  # !

    # String & Character Handling
    DOUBLE_QUOTE = "DOUBLE_QUOTE"  # "
    SINGLE_QUOTE = "SINGLE_QUOTE"  # '
    ESCAPE_SEQUENCE = "ESCAPE_SEQUENCE"  # \n, \t, \r, etc.

    # Special & Miscellaneous Tokens
    NEWLINE = "NEWLINE"  # \n
    TAB = "TAB"  # \t
    SPACE = "SPACE"  #  
    COMMENT = "COMMENT"  # #
    MULTI_COMMENT = "MULTI_COMMENT"  # """ or '''
    ERROR = "ERROR"  # Invalid token
    EOF = "EOF"  # End of file
