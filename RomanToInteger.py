
s = "CD"



def romanToInteger(s):
    symArray = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000
    }
    
    sum = 0
    current = 0
    prev = 0
    
    
    for i in range(len(s)):
        current = symArray[s[i]]
        if current > prev:
            sum = sum + current - 2 * prev;
        else:
            sum +=current
        prev = current
    return sum;




print(romanToInteger(s))