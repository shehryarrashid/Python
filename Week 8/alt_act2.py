def split_string(user_input):
    values = user_input.split(" ")
    if len(values) != 3:
        raise ValueError
    return values


def check_string(user_input):

    if user_input[1] != '+' and user_input[1] != '-':
        raise ValueError
    return True


def calculate(user_input):
    result = 0.0
    if user_input[1] == '+':
        result += float(user_input[0]) + float(user_input[2])
    else:
        result += float(user_input[0]) - float(user_input[2])

    return result


def get_string():
    user_input = input(">>>")
    if user_input == 'quit':
        return False
    return user_input


def main():
    while True:
        user_input = get_string()
        if user_input:
            try:
                values = split_string(user_input)
                check_string(values)
                print(calculate(values))
            except:
                print("Wrong arguments")
        else:
            break
    return 0

main()