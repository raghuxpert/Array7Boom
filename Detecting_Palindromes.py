# These are words or numbers that are read the same forward and backward, like 121.

def is_Palindrome(a):
    j = -1
    for i in range(0,len(a)//2):
        if a[i] != a[j]:
            return False
        j-=1
    return True

def is_Palindrome1(a):
    b = a[len(a)::-1]  # reverse the string
    if a == b:
        return True
    else:
        return False

def is_Palindrome2(a):
    b = ''.join((reversed(a)))     # reverse the string
    if a == b:
        return True
    else:
        return False

a = str(input("insert data : "))
print(is_Palindrome2(a))


