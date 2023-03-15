

def counter(str1):
    print(str1)
    digits, alpha, special = 0, 0, 0
    for i in range(len(str1)):
        if str1[i].isdigit():
            digits += 1
        elif str1[i].isalpha():
            alpha += 1
        else:
            special += 1
    return "Digits: " + str(digits) + " \nChars: " + str(alpha) + "\nSpecials: " + str(special)



