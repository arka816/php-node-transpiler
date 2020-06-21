###LEXER PROGRAM FOR PHP-NODE JS TRANSPILER
### AUTHOR : ARKA
keywords = ["do", "while", "for", "if", "elseif", "else", "try", "catch", "throw", "new", "echo", "function", "class"]

class ASTNode:
    def __init__(self):
        self.type = None
        self.parent = None
        self.childList = []
    def pushChild(self, elem):
        self.childList.append(elem)
        
class whileNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.conditionList = []
        self.body = None
    def addCondition(self, condition):
        self.conditionList.append(condition)
        
class operatorNode(ASTNode):
    def __init__(self):
        super().__init__()
        self.operator = None
        self.operandLeft = None
        self.operandRight = None
        
class variable(ASTNode):
    def __init__(self):
        super().__init__()
        self.name = None
        self.varType = None


root = ASTNode()
root.type = "root"

def classifySegment(segment):
    segment = segment.strip()
    if segment[0] == "$":
        return "variable"
    else:
        keyword = ""
        for i in range(len(segment)):
            char = segment[i]
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                keyword += char
            else:
                break
        if keyword.lower() in keywords:
            return keyword
        else:
            print("error finding keyword in token")

def buildAST(segment):
    print(classifySegment(segment))
    
def generateAST(tokenList):
    for token in tokenList:
        buildAST(token)
        