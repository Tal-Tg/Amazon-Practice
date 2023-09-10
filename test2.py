from ast import Return


s = "|**|*|*"
arrStart = [1, 4]
arrEnd = [4, 6]


def timesOfChar(str):
    i = 0
    count = 0
    while i < len(str):
        if ord(str[i]) == 124:
            count+=1
        i+=1
        
    return count


def getLen(input):
    num_appeared = timesOfChar(input)
    print(f"num of : {num_appeared}")
    count = 0
    if num_appeared == 2:
        result = 0
        for c in input:
            if(c == '|'):
                count+=1
            result += 1
            if count == num_appeared:
                return result-num_appeared
    
    if num_appeared % 2:
        result = 0
        for c in input:
            if(c == '|'):
                count+=1
            result += 1
            if count == num_appeared:
                return result-num_appeared
    
    result = 0
    for c in input:
        if(c == '|'):
            count+=1
        result += 1
        if count == num_appeared-1:
            return result-num_appeared


def numbersOfItems(s,startIndices,endIndices):
    inventorySize = 0
    isInside = False
    currentValue = 0
    print(endIndices[1])
    print(endIndices[0])
    current = startIndices[0]
    k = 0
    while k < len(startIndices):
        newString = s[startIndices[k] -1: endIndices[k]-1]
        print(newString)
        # new_str = ""
        # for i in range(startIndices[k], endIndices[k]):
        #     new_str += i
        print(getLen(newString))
        k+=1
        
        # newString = s[startIndices[i] : endIndices[i]]
        # new_num = getLen(newString)
        # print(new_num)
    
numbersOfItems(s, arrStart, arrEnd)
    
    # while i < len(startIndices):
    #     currentStart = startIndices[i]
    #     currentEnd = endIndices[i]
    #     index = currentStart
    #     while index < currentEnd:
    #         if ord(s[index]) == 124 :
    #             isInside = True
    #             "123cc | 123123 | 12fd |"
    #             "|"
    
    
    
    