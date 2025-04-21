from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

# This is the main entry point for the program.
# It takes user input, processes it through the lexer, parser, and interpreter stages, and outputs results.
def main():
    print("Enter your code (type 'end' to finish):")
    
    # Collect lines of code from the user until they type 'end'
    code_lines = []
    while True:
        line = input("input> ")
        if line.lower() == "end":
            break
        code_lines.append(line)

    # Join all the lines together into one code string
    code = "\n".join(code_lines)

    #      LEXER PHASE
    print("\n====== Lexer Output ======")
    lexer = Lexer(code)
    tokenized_output = lexer.tokenize()

    # Print out the token types for each line of code
    for line_tokens in tokenized_output:
        token_types = [token.type for token in line_tokens]
        print(f"[{', '.join(token_types)}]")

    #      PARSER PHASE
    print("\n====== Parser (AST) Output ======")
    try:
        # Flatten the list of token lists into a single list of tokens for parsing
        parser = Parser([token for line in tokenized_output for token in line])
        ast = parser.parse()

        # Print out the AST nodes for inspection
        for node in ast:
            print(node)

    except SyntaxError as e:
        # If there's a syntax error, display it and stop execution
        print(f"Syntax Error: {e}")
        return

    #     INTERPRETER PHASE
    print("\n====== Interpreter Execution Output ======")
    interpreter = Interpreter()
    interpreter.interpret(ast)

# If this script is being run directly (not imported), execute main()
if __name__ == "__main__":
    main()
