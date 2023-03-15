# In search for the perfect numbers

def number_checker(a):
    sum = 0
    for algo in range(1,a):
        if a % algo == 0:
            sum = sum + algo
    if sum == a:
        return True
    return False

print(number_checker(6))
