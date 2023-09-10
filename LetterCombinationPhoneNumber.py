arr = [["2","abc"],["3","def"],["4", "ghi"],["5","jkl"]
    ,["6","mno"],["7","pqrs"],["8","tuv"],["9","wxyz"]]
target = "23"



def letterCombination(arr,target):
    digitArray = []
    output = []
    for i in range(len(target)):
        for item,val in arr:
            if target[i] == item:
                digitArray.append([item,val])
    # print(digitArray)
    # for i,val1 in digitArray:
    #     print("val1"+val1)
    #     for j,val2 in digitArray:
    #         print("val2"+val2)
    #         # output.append([val1,val2])

    
    return digitArray;
print(letterCombination(arr,target))

