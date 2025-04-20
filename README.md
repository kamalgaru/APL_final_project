# APL_final_project
first of all down the git hub file
open visual studio code and go to the repository path
type python main.py [Hit enter]
Enter your input like the given example
input> let x=10+5;
input> let y=x*2;
input> print(x);  
input> print(y);
input> end [Hit enter]

This will generate output as 
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
15.0
30.0
