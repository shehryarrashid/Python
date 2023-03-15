
def obtain_age():
    while True:
        try:
            user = int(input("Enter the age: "))
            break
        except Exception as e:
            print(e)
    return user

def name_check(name):
    for x in range(len(name)):
        if name[x].isalpha() == False and name[x] != " " :
            return False
    name.capitalize()
    return True


def enter_name():
    while True:
        user = input("Enter your name:")
        if name_check(user):
            break
        else:
            print("Invalid Name")
    return user

def create_user():
    name = enter_name()
    age = obtain_age()
    print(f"New user created \nName: {name} \nAge: {age}")
    return name , age

def main():

    all_users = []
    stop = 0

    while True:
        
        user = []
        user.append(create_user())
        all_users.append(user)
        while True:
            try:
                stop = int(input("\nEnter 0 to Stop: "))
                break
            except Exception as e:
                print(e)
                print("Enter any number to contine")
        if stop == 0:
            break
    
    return all_users

users = main()
print("List of Users")
for user in users:
    print(user)