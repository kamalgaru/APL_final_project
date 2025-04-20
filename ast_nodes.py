class ASTNode:
    """Base class for all AST nodes."""
    pass

class NumberNode(ASTNode):
    """Represents a numeric value."""
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"NumberNode({self.value})"

class VarNode(ASTNode):
    """Represents a variable reference."""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"VarNode({self.name})"

class BinOpNode(ASTNode):
    """Represents a binary operation (e.g., addition, subtraction)."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode(left={self.left}, op={self.op}, right={self.right})"

class AssignNode(ASTNode):
    """Represents a variable assignment statement."""
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f"AssignNode(var={self.var}, expr={self.expr})"

class PrintNode(ASTNode):
    """Represents a print statement."""
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"PrintNode(expr={self.expr})"
