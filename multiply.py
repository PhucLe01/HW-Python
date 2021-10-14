def multiply_list(numList):
    '''
    Calculate the product of a list.

    This function do multiplication on an inputed list.

    parameters
    ----------
    numList : list
             A list of numbers.
    
    return 
    ----------
    int
            The result of multiplication from every member in the list.
        
    '''
    answer = 1
    for number in numList:
        if(isinstance(number, int)):
            answer = answer * number
        else:
            return False
    return answer