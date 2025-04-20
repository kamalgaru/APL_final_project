# APL Final Project – Python Interpreter

This project is a simple **Python-based interpreter** built for an APL (Advanced Programming Languages) final project. It supports variable assignment, arithmetic expressions, and `print()` statements, showing how a custom lexer, parser, and interpreter work together.

---

## 🚀 How to Run

1. **Clone the repository** from GitHub:
   ```bash
   git clone https://github.com/kamalgaru/APL_final_project
   cd APL_final_project

2. Open the repository folder in Visual Studio Code or your preferred code editor.

3. Run the interpreter from the terminal:
   python main.py
   
   🧪 Example Usage
   Once the program is running, enter the following inputs:
   input> let x = 10 + 5;
   input> let y = x * 2;
   input> print(x);
   input> print(y);
   input> end

   ✅ Expected Output
    ====== Lexer Output ======
    [LET, ID, ASSIGN, NUMBER, PLUS, NUMBER, SEMICOLON]
    [LET, ID, ASSIGN, ID, MUL, NUMBER, SEMICOLON]
    [PRINT, LPAREN, ID, RPAREN, SEMICOLON]
    [PRINT, LPAREN, ID, RPAREN, SEMICOLON]

    ====== Parser (AST) Output ======
    [AssignNode(var=x, expr=BinOpNode(left=NumberNode(10), op=PLUS, right=NumberNode(5)))]
    [AssignNode(var=y, expr=BinOpNode(left=VarNode(x), op=MUL, right=NumberNode(2)))]
    PrintNode(expr=VarNode(x))
    PrintNode(expr=VarNode(y))

    ====== Interpreter Execution Output ======
    15
    30


