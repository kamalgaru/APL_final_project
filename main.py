from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

# Main function this is the entry point of the program.
# Hndles user input, tokenization, parsing, and interpretation.
def main():
    # Prompt user for code input line-by-line until they type 'end'
    print("Enter your code (type 'end' to finish):")
    code_lines = []
    while True:
        line = input("input> ")
        if line.lower() == "end":
            break
        code_lines.append(line)

    # Combine all entered lines into a single code string
    code = "\n".join(code_lines)

    # ----- LEXER PHASE -----
    # Convert raw code into a list of tokens
    print("\n====== Lexer Output ======")
    lexer = Lexer(code)
    tokenized_output = lexer.tokenize()

    # Display the token types generated for each line
    for line_tokens in tokenized_output:
        token_types = [token.type for token in line_tokens]
        print(f"[{', '.join(token_types)}]")

    # ----- PARSER PHASE -----
    # Convert tokens into an Abstract Syntax Tree (AST)
    print("\n====== Parser (AST) Output ======")
    try:
        # Flatten tokenized lines into a single list of tokens
        parser = Parser([token for line in tokenized_output for token in line])
        ast = parser.parse()
        for node in ast:
            print(node)
    
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return

    # ----- INTERPRETER PHASE -----
    # Execute the AST, performing the program's logic
    print("\n====== Interpreter Execution Output ======")
    interpreter = Interpreter()
    interpreter.interpret(ast)

# Ensures the main function runs when this file is executed directly
if __name__ == "__main__":
    main()
