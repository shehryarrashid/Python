
def calculate(sweet, pupil):

    if(type(sweet) == int and type(pupil) == int):

        if(sweet<=0 or pupil <= 0):
            return "You have entered a wrong number of sweets or pupils"
        else:
            sweets_each = round(sweet / pupil)
            left_over = sweet % pupil
            statement = 'Each pupil gets: ' + str(sweets_each) +' sweets and there are '+ str(left_over) +' sweets left over'
            return statement
    else:
        return "Incorrect Type"


print(calculate(35,15))
print(calculate(47,16))
print(calculate("hello",15))