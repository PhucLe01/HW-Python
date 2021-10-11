def multiply_list(numList):
    answer = 1
    for number in numList:
        if(isinstance(number, int)):
            answer = answer * number
        else:
            return False
    return answer