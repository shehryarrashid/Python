def function(x):
    y = 6 * x**2 + 3*x + 2
    return y


def shut_down(s):
    awn = ""
    if s == "yes":
        awn += "Shutting Down"
    elif s == "no":
        awn += "Shutdown aborted"
    else:
        awn += "Sorry"
    return awn


def distance_from_zero(arg):

    if type(arg) == int or type(arg) == float:
        return abs(arg)
    return "Nope"


def rate_calculator(hours, rate):
    extra_hours = hours - 40
    pay = 0
    if extra_hours > 0:
        pay = 40 * rate
        pay += extra_hours * rate * 1.5
    else:
        pay = hours * rate
    return pay


def user_part1():

    hours = int(input("Enter Hours: "))
    rate = int(input("Rate: "))
    return rate_calculator(hours,rate)


while True:
    try:
        print(user_part1())
        break

    except ValueError:
        print("Wrong Arguments")



