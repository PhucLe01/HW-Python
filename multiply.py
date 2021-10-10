def multiply_list(list):
    answer = 1
    for number in list:
        if(isinstance(number, int)):
            answer = answer * number
        else:
            return False
    return answer

def main():
    list1 = [1, 2, 3, 7]
    print(multiply_list(list1))

main()