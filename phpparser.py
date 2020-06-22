###LEXER PROGRAM FOR PHP-NODE JS TRANSPILER
### AUTHOR : ARKA
import sys

keywords = ["do", "while", "for", "if", "elseif", "else", "try", "catch", "throw", "new", "echo", "function", "class"]
comparisonOp = ["===", "!==", "==", "!=", ">=", "<=", ">", "<", "<>", "<=>"]
logicalOp = ["and", "or", "&&", "||", "xor", "!"]

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

root = ASTNode()
root.type = "root"

def removeRedundantParentheses(string):
    ### REMOVES REDUNDANT PAIRS OF PARENTHESES FROM START AND END OF STRING
    flag = True
    while(flag):
        flag = False
        codeflag = True
        stack = []
        j = string.find("(")
        if j >= 0:
            for i in range(j + 1, len(string)):
                char = string[i]
                if char == "\"" and string[i-1] != "\\":
                    codeflag = not codeflag
                elif char == "(" and codeflag:
                    stack.append("(")
                elif char == ")" and codeflag:
                    if len(stack) == 0:
                        if i == len(string) - 1:
                            string = string[0 : j] + string[j + 1: i] + string[i + 1 : len(string)]
                            flag = True
                            break
                        else:
                            flag = False
                    else:
                        stack.pop()
    
    return string


def evaluate(segment):
    return segment

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

def parseCondition(statement, parentNode):
    ### CLEANSE STRING
    statement = statement.strip()
    ### REMOVE REDUNDANT PARENTHESES FROM STRING
    statement = removeRedundantParentheses(statement)
    
    ### FIND THE FIRST EXTERNAL LOGICAL OPERATOR
    ### AND THEN STRIP THE OPERATOR AND OPERAND
    if statement[0] == "(":
        ### STRIP THE LEFT OPERAND
        stack = []
        stack.append("(")
        flag = True
        for i in range(1, len(statement)):
            char = statement[i]
            if len(stack) == 0:
                searchstring = statement[i : len(statement)].strip()
                break
            if char == "(" and flag:
                stack.append("(")
            elif char == ")" and flag:
                stack.pop()
            elif char == "\"" and statement[i-1] != "\\":
                flag = not flag
        operandLeft = statement[0:i].strip()
        
        ### STRIP THE OPERATOR
        operator = ""
        for i in range(len(searchstring)):
            c=searchstring[i]
            if c == " " or c == "$" or c == "(":
                break
            else:
                operator += c
                
        ### STRIP THE RIGHT OPERAND
        operandRight = searchstring[i:len(searchstring)].strip()
        
        if operator not in logicalOp:
            print("invalid operator")
            sys.exit()
            
        parentNode.operator = operator
        parentNode.operandLeft = operandLeft
        parentNode.operandRight = operandRight
        

    print(statement)
    return parentNode




def buildAST(segment):
    l=len(segment)
    keyword = classifySegment(segment)
    if keyword == "variable":
        ### THE SEGMENT IS AN ASSIGNMENT STATEMENT
        operatorNode = OperatorNode()
        identifierNode = IdentifierNode()
        i = segment.find("=")
        operatorNode.operator = "="
        identifierNode.name = segment[0: i].strip()
        operatorNode.operandLeft = identifierNode
        operatorNode.operandRight = evaluate(segment[i+1: l].strip())
        operatorNode.parent = root
        root.pushChild(operatorNode)
        
    elif keyword == "while":
        whileNode = WhileNode() ### NODE FOR THE WHILE LOOP SEGMENT
        conditionNode = OperatorNode() ### NODE FOR THE CONDITION SEGMENT
        bodyNode = ASTNode() ### NODE FOR THE BODY OF THE WHILE LOOP
        codeflag = True
        ### EXTRACT THE CONDITION
        stack = []
        f = segment.find("(")
        stack.append("(")
        i=f
        while i < l:
            if len(stack) == 0:
                break
            i += 1
            char = segment[i]
            if char == "(" and codeflag:
                stack.append("(")
                print
            elif char == ")" and codeflag:
                stack.pop()
            elif char == "\"" and segment[i-1] != "\\":
                codeflag = not codeflag
         
        whileNode.condition = parseCondition(segment[f+1: i], conditionNode)
        ### EXTRACT THE BODY
        whileNode.parent = root
        root.pushChild(whileNode)


def generateAST(tokenList):
    for token in tokenList:
        buildAST(token)
    return root
        