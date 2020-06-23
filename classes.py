class ASTNode:
    def __init__(self):
        self.type = None
        self.parent = None
        self.childList = []
    def pushChild(self, elem):
        self.childList.append(elem)
        
class WhileNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.condition = None
        self.body = None
        
class OperatorNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.operator = None
        self.operandLeft = None
        self.operandRight = None
        
class IdentifierNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.name = None
        self.varType = None

class ValueNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.value = None
        self.varType = None