from ast_nodes import AssignNode, PrintNode, BinOpNode, VarNode, NumberNode
class Interpreter:
    def __init__(self):
        self.vars = {}

    def execute(self, statements):
        for statement in statements:
            if isinstance(statement, AssignNode):
                self.execute_assign(statement)
            elif isinstance(statement, PrintNode):
                self.execute_print(statement)
            else:
                raise Exception(f'Unknown statement type: {type(statement)}')

    def execute_assign(self, node):
        value = self.evaluate(node.expr)
        self.vars[node.var_name] = value

    def execute_print(self, node):
        value = self.evaluate(node.expr)
        print(value)

    def evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, VarNode):
            if node.name in self.vars:
                return self.vars[node.name]
            else:
                raise NameError(f"Variable '{node.name}' not defined")
        elif isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == 'PLUS':
                return left + right
            elif node.op == 'MINUS':
                return left - right
            elif node.op == 'MUL':
                return left * right
            elif node.op == 'DIV':
                return left / right
            else:
                raise Exception(f"Unknown operator {node.op}")
        else:
            raise Exception(f"Unknown node type: {type(node)}")