###LEXER PROGRAM FOR PHP-NODE JS TRANSPILER
### GENERATES TOKENS FOR PARSING
### AUTHOR : ARKA
### isTokenFlag determines if current character belongs to code or is it part of a string
### isExFlag determines if current character belongs to a code segment e.g. function or class
### or for loop or method or is it purely external token


def tokenizer(string):
    tokenList = []
    isTokenFlag = True
    isExFlag = True
    lastTokenIndex = 0
    stack = []
    l = len(string)
    i=0
    while i < l:
        char=string[i]
        if char == ";" and isTokenFlag and isExFlag:
            tokenList.append(string[lastTokenIndex : i].strip())
            lastTokenIndex = i+1
        elif char == "(" and isTokenFlag:
            if len(stack) == 0:
                isExFlag = not isExFlag
            stack.append("(")
        elif char == ")" and isTokenFlag:
            stack.pop()
            if len(stack) == 0:
                #segment ends
                isExFlag = not isExFlag
        elif char == "{" and isTokenFlag:
            if len(stack) == 0:
                isExFlag = not isExFlag
            stack.append("{")
        elif char == "}" and isTokenFlag:
            stack.pop()
            if len(stack) == 0:
                #segment ends
                isExFlag = not isExFlag
                tokenList.append(string[lastTokenIndex : i+1].strip())
                lastTokenIndex = i+1
        elif char == "/" and isTokenFlag:
            if string[i+1] == "*":
                #it is a comment
                i = string.find("*/", i+2, l) + 2
                lastTokenIndex = i
                continue
            elif string[i+1] == "/":
                #it is a comment
                i = string.find("\n", i+2, l) + 1
                lastTokenIndex = i
                continue
        elif char == "#" and isTokenFlag:
            #it is a comment
            i = string.find("\n", i+1, l) + 1
            lastTokenIndex = i
            continue
        elif char == "\"" and string[i-1] != "\\":
            isTokenFlag = not isTokenFlag
        i += 1
    return tokenList       