from ast_nodes import *

# Interpreter class 
class Interpreter:
    def __init__(self):
        
        self.variables = {} # Store variables and their assigned values

    def interpret(self, nodes):  # Main function for interpret a list of AST nodes
        for node in nodes:
            if isinstance(node, list): # In case node is a list suh as nested statements, handle each sub-node
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
                print(f"Error: Variable '{node.name}' is not defined.")
                exit(1)

        elif isinstance(node, BinOpNode):
            # Recursively evaluate the left and right sides of the binary operation
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            # Convert string numbers to float if required
            left = float(left) if isinstance(left, str) else left
            right = float(right) if isinstance(right, str) else right

            if node.op == 'PLUS':
                result = left + right
            elif node.op == 'MINUS':
                result = left - right
            elif node.op == 'MUL':
                result = left * right
            elif node.op == 'DIV':
                result = left / right
            else:
                print(f"Error: Unknown operator '{node.op}'.") # Print unknown operators
                exit(1)
            
            if isinstance(left, int) and isinstance(right, int): # If both operands were integers, return an integer value
                return int(result)

            return result

        else:
            print(f"Error: Unknown node type '{type(node)}'.") # Catch unrecognize node type
            exit(1)
