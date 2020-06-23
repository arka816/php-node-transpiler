keywords = ["do", "while", "for", "if", "elseif", "else", "try", "catch", "throw", "new", "echo", "function", "class"]
comparisonOp = ["===", "!==", "==", "!=", ">=", "<=", ">", "<", "<>", "<=>"]
logicalOp = ["and", "or", "&&", "||", "xor"]


def classifySegment(segment):
    ### CLASSIFIES A TOKEN RECEIVED FROM LEXER
    segment = segment.strip()
    if segment[0] == "$":
        return "identifier"
    else:
        keyword = ""
        for char in segment:
            if char.isalpha():
                keyword += char
            else:
                break
        if keyword.lower() in keywords:
            return keyword
        else:
            print("error finding keyword in token")
            
def removeRedundantParentheses(string):
    ### REMOVES REDUNDANT PAIRS OF PARENTHESES FROM START AND END OF STRING
    print("rrp ", string)
    if string[0] != "(":
        return string
    while(string[0] == "("):
        codeflag = True
        stack = []
        for i in range(1, len(string)):
            char = string[i]
            if char == "\"" and string[i-1] != "\\":
                codeflag = not codeflag
            elif char == "(" and codeflag:
                stack.append("(")
            elif char == ")" and codeflag:
                if len(stack) == 0:
                    if i == len(string) - 1:
                        string = string[1 : i]
                        break
                    else:
                        return string
                else:
                    stack.pop()
    return string

def findLogicalOperator(operator, string):
    ### FINDS THE FIRST LOGICAL OPERATOR IN A COMPOUND CONDITIONAL STATEMENT
    ### GIVEN THAT THE FIRST CONDITION IS NOT PARENTHESISED
    flag = True
    M = len(operator)
    N = len(string)
    if operator in ["and", "or", "xor"]:
        ### FOR ALPHABETICAL FORMAT LOGICAL OPERATORS
        for i in range(N - M + 1):
            if string[i] == "\"" and string[i-1] != "\\":
                flag = not flag
            if flag:
                j = 0
                while j < M:
                    if string[i + j] != operator[j]:
                        break
                    else:
                        j += 1
                if j == M:
                    c = string[i-1]
                    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == "$" or c == "_":
                        pass
                    else:
                        return i
            else:
                continue
        return N
    else:
        ### FOR NON-ALPHABETICAL LOGICAL OPERATORS
        for i in range(N - M + 1):
            if string[i] == "\"" and string[i-1] != "\\":
                flag = not flag
            if flag:
                j = 0
                while j < M:
                    if string[i + j] != operator[j]:
                        break
                    else:
                        j += 1
                if j == M:
                    return i
            else:
                continue
        return N

def findComparisonOperator(operator, string):
    ### FINDS THE ONLY COMPARISON OPERATOR IN A SIMPLE CONDITION STATEMENT
    flag = True
    M = len(operator)
    N = len(string)
    for i in range(N - M + 1):
        if string[i] == "\"" and string[i-1] != "\\":
            flag = not flag
        if flag:
            j = 0
            while(j < M):
                if string[i + j] != operator[j]:
                    break
                else:
                    j += 1
            if j == M:
                return i
        else:
            continue
    return -1
