import random
from datetime import *
import act_1

def tip_perc():
    good = act_1.try_input("If service was bad enter 0 else any number: ", int)
    if good:
        return 0.15
    return 0


def meal(cost):
    tax_per = 0.0675
    cost += (cost*tax_per)
    tip = tip_perc()
    cost += cost * tip
    return cost


# print("%.2f" % meal(200))


def showtime(given_date):

    return given_date.strftime("%m/%d/%Y %I:%M:%S")


print(datetime.now())
# print(act_1.add_days(datetime(2002, 9, 29, 7, 0, 0), 7))


def one_number():
    number = []
    for x in range(10):
        number.append(random.randint(0, 9))
    return number



def check_if_in(all_lotterys, number):
    if number in all_lotterys:
        return True
    return False


def all_numbers():
    all_lotterys = []
    for y in range(100):
        number = one_number()
        if not check_if_in(all_lotterys, number):
            all_lotterys.append(number)
        else:
            y -= 1
    return all_lotterys

# print(all_numbers())


def generate_winners():
    number_list = all_numbers()
    winners = act_1.try_input("Enter number of winners: ", int)
    all_winners = []
    while winners:
        rand = act_1.random_number()
        all_winners.append(number_list[rand])
        winners -= 1
    return all_winners

def print_numers():
    strin = ""
    for x in generate_winners():
        for y in x:
            strin += str(y)
        print(strin)
        strin = ""


