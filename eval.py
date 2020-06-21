# ARITHMETIC STRING EVALUATION PROGRAM
# AUTHOR ARKA

import sys
import math

stack=[]
degflag = True

def factorial(n):
    n=int(n)
    if n==1 or n==0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact
        

def evalRec(string):
    global stack, degflag
    if 'sin' in string:
        while string.find('sin') != -1:
            l=len(string)
            index = string.find("sin")
            if string[index+3] == "(":
                stack.append("(")
                i=index + 3
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                argument = string[index+3: end+1]
            else:
                print("no brackets after sin call")
                sys.exit()
            angle=float(eval(argument))
            if degflag:
                angle = float(angle * math.pi / 180)
            string = string[0:index] + str(math.sin(angle)) + string[end+1: len(string)]
        return eval(string)
    elif 'cos' in string:
        while string.find('cos') != -1:
            l=len(string)
            index = string.find("cos")
            if string[index+3] == "(":
                stack.append("(")
                i=index + 3
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                argument = string[index+3: end+1]
            else:
                print("no brackets after cos call")
                sys.exit()
            angle=float(eval(argument))
            if degflag:
                angle = float(angle * math.pi / 180)
            string = string[0:index] + str(math.cos(angle)) + string[end+1: len(string)]
        return eval(string)
    elif 'tan' in string:
        while string.find('tan') != -1:
            l=len(string)
            index = string.find("tan")
            if string[index+3] == "(":
                stack.append("(")
                i=index + 3
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                argument = string[index+3: end+1]
            else:
                print("no brackets after tan call")
                sys.exit()
            angle=float(eval(argument))
            if degflag:
                angle = float(angle * math.pi / 180)
            string = string[0:index] + str(math.tan(angle)) + string[end+1: len(string)]
        return eval(string)
    elif 'ln' in string:
        while string.find('ln') != -1:
            l=len(string)
            index = string.find("ln")
            if string[index+2] == "(":
                stack.append("(")
                i=index + 2
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                argument = string[index+2: end+1]
            else:
                print("no brackets after ln call")
                sys.exit()
            string = string[0:index] + str(float(math.log(eval(argument)))) + string[end+1: len(string)]
        return eval(string)
    elif 'log' in string:
        while string.find('log') != -1:
            l=len(string)
            index = string.find("log")
            if string[index+3] == "(":
                stack.append("(")
                i=index + 3
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                argument = string[index+3: end+1]
            else:
                print("no brackets after log call")
                sys.exit()
            string = string[0:index] + str(float(math.log(eval(argument), 10))) + string[end+1: len(string)]
        return eval(string)
    elif "!" in string:
        while string.find('!') != -1:
            l=len(string)
            index = string.find("!")
            if string[index-1] == ")":
                stack.append(")")
                i=index - 1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                number = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                number = string[start:index]
            string = string[0:start] + str(int(factorial(eval(number)))) + string[index+1: len(string)]
        return eval(string)
    elif "^" in string:
        while string.find('^') != -1:
            l=len(string)
            index = string.find("^")
            if string[index-1] == ")":
                stack.append(")")
                i=index - 1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                base = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                base = string[start:index]
            if string[index+1] == "(":
                stack.append("(")
                i=index + 1
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                exponent = string[index+1: end+1]
            else:
                i=index+1
                while i < l and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i+=1
                end = i-1
                exponent = string[index+1: end+1]
            string = string[0:start] + str(float(eval(base) ** eval(exponent))) + string[end+1: len(string)]
        return eval(string)
    elif "/" in string:
        while string.find('/') != -1:
            l=len(string)
            index = string.find("/")
            if string[index-1] == ")":
                stack.append(")")
                i=index - 1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                dividend = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                dividend = string[start:index]
            if string[index+1] == "(":
                stack.append("(")
                i=index + 1
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                divisor = string[index+1: end+1]
            else:
                i=index+1
                while i < l and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i+=1
                end = i-1
                divisor = string[index+1: end+1]
            string = string[0:start] + str(format(float(eval(dividend) / eval(divisor)), '.6f')) + string[end+1: len(string)]
        return eval(string)
    elif "*" in string:
        while string.find('*') != -1:
            l=len(string)
            index = string.find("*")
            if string[index-1] == ")":
                stack.append(")")
                i=index - 1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                multiplicand = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                multiplicand = string[start:index]
            if string[index+1] == "(":
                stack.append("(")
                i=index+1
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                multiplier = string[index+1: end+1]
            else:
                i=index+1
                while i < l and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i+=1
                end = i-1
                multiplier = string[index+1: end+1]
            string = string[0:start] + str(float(eval(multiplicand) * eval(multiplier))) + string[end+1: len(string)]
        return eval(string)
    elif "+" in string:
        while string.find('+') != -1:
            l=len(string)
            index = string.find("+")
            if string[index-1] == ")":
                stack.append(")")
                i=index-1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                addend = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                addend = string[start:index]
            if string[index+1] == "(":
                stack.append("(")
                i=index+1
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                adder = string[index+1: end+1]
            else:
                i=index+1
                while i < l and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i+=1
                end = i-1
                adder = string[index+1: end+1]
            string = string[0:start] + str(float(eval(addend) + eval(adder))) + string[end+1: len(string)]
        return eval(string)
    elif "-" in string:
        while string.find('-') != -1:
            l=len(string)
            index = string.find("-")
            if string[index-1] == ")":
                stack.append(")")
                i=index-1
                while len(stack) > 0 and i > 0:
                    i -= 1
                    if string[i] == ")":
                        stack.append(")")
                    elif string[i] == "(":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                start = i
                minuend = string[start:index]
            else:
                i = index - 1
                while i >= 0 and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i-=1
                start=i+1
                minuend = string[start:index]
            if string[index+1] == "(":
                stack.append("(")
                i=index+1
                while len(stack) > 0 and i < l - 1:
                    i += 1
                    if string[i] == "(":
                        stack.append("(")
                    elif string[i] == ")":
                        try:
                            stack.pop()
                        except:
                            print("invalid bracket structure")
                            sys.exit()
                end = i
                subtrahend = string[index+1: end+1]
            else:
                i=index+1
                while i < l and ((string[i] >= '0' and string[i] <= '9') or string[i] == "."):
                    i+=1
                end = i-1
                subtrahend = string[index+1: end+1]            
            string = string[0:start] + str(float(eval(minuend) - eval(subtrahend))) + string[end+1: len(string)]
        return eval(string)
    else:
        string = string.strip("(").strip(")")
        f=float(string)
        return f
                
    
def evalStr(string):
    string=string.replace(" ", "")
    return evalRec(string)
        