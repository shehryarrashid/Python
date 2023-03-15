def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

def fir_mid_last(str1):
    len = string_length(str1)
    fir = str1[0]
    fir += str1[int(len/2)]
    fir += str1[-1]
    return fir

def ocurrences(org_str,word):
    ok = False
    occur = 0
    try:
        org_copy = org_str.lower()
        word_lower = word.lower()
        occur = org_copy.count(word_lower)
        ok = True
    except Exception as error:
        print(error)

    if(ok):
        return occur
    
def reverse(str1):
    # Both Methods Work
    #rev = str1[::-1]
    #for i in range(len(str1)-1,-1,-1):
    #    rev += str1[i]
    rev = "".join(reversed(str1))
    return rev

print(reverse("Shehryar"))
    

