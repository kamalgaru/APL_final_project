from ast_nodes import *

# Interpreter class — responsible for executing the AST produced by the parser
class Interpreter:
    def __init__(self):
        # Dictionary to store variables and their assigned values
        self.variables = {}

    # Main method to interpret a list of AST nodes
    def interpret(self, nodes):
        for node in nodes:
            # In case node is a list (e.g., nested statements), handle each sub-node
            if isinstance(node, list):
                for sub_node in node:
                    self.execute(sub_node)
            else:
                self.execute(node)

    # Executes a single AST node
    def execute(self, node):
        if isinstance(node, AssignNode):
            # Evaluate the right-hand side expression
            value = self.evaluate(node.expr)
            # Assign the evaluated value to the variable in the variables dictionary
            self.variables[node.var] = value

        elif isinstance(node, PrintNode):
            # Evaluate the expression and print its value
            value = self.evaluate(node.expr)
            print(value)

    # Recursively evaluates an AST node and returns the resulting value
    def evaluate(self, node):
        if isinstance(node, NumberNode):
            # Return the numeric value directly
            return node.value

        elif isinstance(node, VarNode):
            # Retrieve the value of the variable from the variables dictionary
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                # Handle undefined variable error
                print(f"Error: Variable '{node.name}' is not defined.")
                exit(1)

        elif isinstance(node, BinOpNode):
            # Recursively evaluate the left and right sides of the binary operation
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            # Convert string numbers to float if necessary
            left = float(left) if isinstance(left, str) else left
            right = float(right) if isinstance(right, str) else right

            # Perform the operation based on the operator type
            if node.op == 'PLUS':
                result = left + right
            elif node.op == 'MINUS':
                result = left - right
            elif node.op == 'MUL':
                result = left * right
            elif node.op == 'DIV':
                result = left / right
            else:
                # Handle unknown operators
                print(f"Error: Unknown operator '{node.op}'.")
                exit(1)

            # If both operands were integers, return an integer result
            if isinstance(left, int) and isinstance(right, int):
                return int(result)

            # Return the result as a float otherwise
            return result

        else:
            # Catch-all for unrecognized node types
            print(f"Error: Unknown node type '{type(node)}'.")
            exit(1)
