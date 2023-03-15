def two_end(str1):
    result = ""
    length = len(str1)
    if length > 2:
        result += str1[0:2]
        result += str1[-2:]
    elif length == 2:
        result += 2 * str1
    return result


def chars(str1):
    first = str1[0]
    listed = list(str1)
    for i in range(1,len(str1)):
        if listed[i] == first:
            listed[i] = "$"
    str1 = "".join(listed)
    return str1


def splitting(str1, str2):

    aux1, aux2 = str1[:2],str2[:2]

    str1 = aux2 + str1[2:]
    str2 = aux1 + str2[2:]

    new = str1 + " " + str2
    return new


def newing(str1):
    if len(str1) >= 3 and str1[-3:] != "ing":
        str1 += "ing"
    elif len(str1) >= 3 and str1[-3:] == "ing":
        str1 += "ly"

    return str1


def upper_lower(str1):

    lowers = []
    uppers = []
    for x in range(len(str1)):
        if str1[x].isupper():
            uppers.append(str1[x])
        elif str1[x].islower():
            lowers.append(str1[x])

    str1 = "".join(lowers) + "".join(uppers)
    return str1




