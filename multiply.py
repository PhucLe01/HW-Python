def multiply_list(list):
    answer = 1
    for number in list:
        if(isinstance(number, int)):
            answer = answer * number
        else:
            return False
    return answer