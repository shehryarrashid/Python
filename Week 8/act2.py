# This program needs to be checked


# This function gets the opeartioon and return every element in form of a list
def get_string():

    log = input("Enter operation: ")
    values = log.split(" ")
    if len(values) != 3:
        raise ValueError

    return values


# This function returns the two numbers
def get_numbers():
    while True:
        try:
            string_inputs = get_string()
            value1, value2 = check_nums(string_inputs)
            break
        except Exception as e:
            print("Wrong arguments")

    return value1, value2, string_inputs[1]


def check_nums(string_inputs):

    value1 = float(string_inputs[0])
    value2 = float(string_inputs[2])

    return value1, value2


def operation_check(inpo):
    if inpo != '+' and inpo != '-':
        raise ValueError


def do_it():
    value1,value2,op = get_numbers()
    try:
        operation_check(op)
        if op == '+':
            print( value1 + value2 )
        else:
            print( value1 - value2 )
    except ValueError:
        print("You entered a wrong operator")

    quite = input("Enter quit/anyting else: ")
    if quite != "quit":
        do_it()


do_it()

