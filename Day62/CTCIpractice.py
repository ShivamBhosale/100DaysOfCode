
import unittest
def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True
    return True
print(unique("Helo"))

def pal_perm(phrase):
    phrase = phrase.replace(" ", "").lower()

    d = dict()

    for i in phrase:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True

print(pal_perm("racecar"))

def UrLify(str1,length):
    str1 = str1[:len(str1)-(len(str1)-length)]
    str1=str1.replace(" ","%20")
    return str1
    

print(UrLify("Mr John Smith    ",13))

def check_permutation(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    if len(str1) != len(str2):
        return False
    else:
        if(sorted(str1) == sorted(str2)):
            return True
        
    return False
        
print(check_permutation("Hello","lloeHt"))