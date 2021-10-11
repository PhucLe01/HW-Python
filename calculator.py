def calculator(number1, number2, operator):
    number1 = float(number1)
    number2 = float(number2)
    if(operator == "+"):
        return number1 + number2
    elif(operator == "-"):
        return number1 - number2
    elif(operator == "*"):
        return number1 * number2
    elif(operator == "/"):
        return number1 / number2
    elif(operator == "//"):
        return number1 // number2
    elif(operator == "**"):
        return number1 ** number2

def parse_input():
    eq = input("Enter equation: ")
    eqList = eq.split()
    in1 = eqList[0]
    op = eqList[1]
    in2 = eqList[2]
    validOperator = ["+", "-", "*", "/", "//", "**"]
    if(op in validOperator):
        return calculator(in1, in2, op)
    else:
        return False