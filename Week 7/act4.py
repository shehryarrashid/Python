def onlynums(str1):
    nums = []
    for i in range(len(str1)):
        if str1[i].isdigit():
            nums.append(str1[i])
    return "".join(nums)

print(onlynums('I am 19 years and 10 months old'))