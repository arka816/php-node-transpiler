###LEXER PROGRAM FOR PHP-NODE JS TRANSPILER
### AUTHOR : ARKA
import sys
from utility import *
from classes import *

keywords = ["do", "while", "for", "if", "elseif", "else", "try", "catch", "throw", "new", "echo", "function", "class"]
comparisonOp = ["===", "!==", "==", "!=", ">=", "<=", ">", "<", "<>", "<=>"]
logicalOp = ["and", "or", "&&", "||", "xor"]


root = ASTNode()
root.type = "root"


def evaluate(segment):
    return segment



def parseCondition(statement, parentNode):
    ### CLEANSE STRING
    statement = statement.strip()
    ### REMOVE REDUNDANT PARENTHESES FROM STRING
    statement = removeRedundantParentheses(statement)
    
    ### FIND THE FIRST EXTERNAL LOGICAL OPERATOR
    ### AND THEN STRIP THE OPERATOR AND OPERAND
    if statement[0] == "(":
        ### EXTRACT THE LEFT OPERAND
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
        
        ### EXTRACT THE OPERATOR
        operator = ""
        for i in range(len(searchstring)):
            c=searchstring[i]
            if c == " " or c == "$" or c == "(" or (c >= "0" and c <= "9") or c == "\"":
                break
            else:
                operator += c
                
        ### EXTRACT THE RIGHT OPERAND
        operandRight = searchstring[i:len(searchstring)].strip()
        
        if operator not in logicalOp:
            print("invalid operator")
            sys.exit()
            
        parentNode.operator = operator
        leftOperandNode = OperatorNode()
        rightOperandNode = OperatorNode()
        parentNode.operandLeft = parseCondition(operandLeft, leftOperandNode)
        parentNode.operandRight = parseCondition(operandRight, rightOperandNode)
        
    else:
        ### THIS CAN BE EITHER A SINGLE OR COMPOUND LOGICAL STATEMENT
        ### FIND THE FIRST LOGICAL OPERATOR...FUCK BRACKETS
        ### IF NO LOGICAL OPERATOR IS FOUND THEN SINGLE STATEMENT
        opDict = dict()
        for lo in logicalOp:
            opDict[lo] = findLogicalOperator(lo, statement)
            
        minIndex = min(opDict.values())
        if minIndex == len(statement):
            ### SINGLE LOGIC STATEMENT
            for comp in comparisonOp:
                i = findComparisonOperator(comp, statement)
                if i >= 0:
                    parentNode.operator = comp
                    parentNode.operandLeft = statement[0 : i].strip()
                    parentNode.operandRight = statement[i + len(comp) : len(statement)].strip()
                    print(comp, parentNode.operandLeft, parentNode.operandRight)
                    break
        else:
            operator = [key for key in opDict if opDict[key] == minIndex]   
            operator = operator[0].strip()
            if operator not in logicalOp:
                print("invalid operator")
                sys.exit()
            
            ### EXTRACT THE LEFT OPERAND
            operandLeft = statement[0 : minIndex].strip()
            ### EXTRACT THE RIGHT OPERAND
            operandRight = statement[minIndex + len(operator) : len(statement)].strip()
            
            parentNode.operator = operator
            leftOperandNode = OperatorNode()
            rightOperandNode = OperatorNode()
            parentNode.operandLeft = parseCondition(operandLeft, leftOperandNode)
            parentNode.operandRight = parseCondition(operandRight, rightOperandNode)
    return parentNode




def buildAST(segment):
    l=len(segment)
    keyword = classifySegment(segment)
    if keyword == "identifier":
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
        