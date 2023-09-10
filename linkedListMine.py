


# l1 = [2,4,3]
# l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


def makeAString(arr):
    stringArr = ""
    for item in arr:
        stringArr += str(item)
    return stringArr;

def addTwoNumbers(l1, l2):
    stringL1 = makeAString(l1)
    stringL2 = makeAString(l2)
    result = int(stringL1) + int(stringL2)
    resultStr = str(result);
    listReturn = [];
    for item in resultStr:
            listReturn.append(item)
    return listReturn[::-1];




print(addTwoNumbers(l1,l2));