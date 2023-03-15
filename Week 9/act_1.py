from datetime import date, datetime, timedelta
import random as rand
import calendar
import random
import string


def today():
    now = date.today()
    # %a = Day
    return now.strftime("%a,%d %B,%Y")


def strtoDate():

    #   %b Month, %d Day, %Y year, %I: Hour, %M minutes, %p PM/AM

    date_string = "Nov 25 2021 4:30PM"
    datetime_object = datetime.strptime(date_string,'%b %d %Y %I:%M%p')
    return datetime_object


def random_number():
    return rand.randint(1,100)


def substract_days(given_date, num):

    resulting_date = given_date - timedelta(days=num)
    resulting_date = datetime.strftime(resulting_date,'%a, %d %b, %Y')
    return str(num) + " Days before was: \n" + str(resulting_date)


def add_days(given_date, num):

    resulting_date = given_date + timedelta(days=num)

    return "Given date: " + str(given_date) + "\n" + str(num) + \
           " Days after will be: \n" + str(resulting_date)


def try_input(messag,type):
    while True:
        try:
            num = type(input(messag))
            break
        except Exception as e:
            print(e)

    return num


def get_Weekday():
    # Return an Integer and Weekday String
    return today.today().weekday(), today.strftime('%A')


def random_pass():

    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource,6)
    password += random.sample(string.ascii_uppercase,2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = "".join(passwordList)
    return password


# print("Random Password is: ",random_pass())





