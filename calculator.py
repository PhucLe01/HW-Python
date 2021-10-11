def calculator(number1, number2, operator):
    number1 = float(number1)
    number2 = float(number2)
    validOperator = ["+", "-", "*", "/", "//", "**"]
    if(operator in validOperator):
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
    else:
        return False

def parse_input():
    eq = input("Enter equation: ")
    eqList = eq.split()
    in1 = eqList[0]
    op = eqList[1]
    in2 = eqList[2]
    calculator(in1, in2, op)