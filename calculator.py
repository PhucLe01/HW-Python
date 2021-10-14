def calculator(number1, number2, operator):
    '''
    Calculate a function of two numbers.

    This function do calculation on two numbers based on the inut operator.

    Parameters
    ----------
    number1 : float
            First input number.
    number2 : float
            Second input number.
    operator : string
            Fuction operator to perform on the 2 input values

    return
    ---------
    float
            The result of the math calculation
    '''
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
            if(number2 != 0):
                return number1 / number2
            else:
                return False
        elif(operator == "//"):
            if(number2 != 0):
                return number1 // number2
            else: 
                return False
        elif(operator == "**"):
            return number1 ** number2
    else:
        return False

def parse_input():
    '''
    Take the math function from user and calculate

    This function prompt the user to input a string of the math function and calculate the answer
    '''
    eq = input("Enter equation: ")
    eqList = eq.split()
    in1 = eqList[0]
    op = eqList[1]
    in2 = eqList[2]
    calculator(in1, in2, op)