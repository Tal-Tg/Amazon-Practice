from click import argument


array = [-4, 3, -9, 0, 4, 1]



def plusMinus(arr):
    arrSize = len(arr);
    newArr = []
    for item in arr:
        newArr.append(str(item))
    plusNumbers = 0;
    minusNumber = 0;
    zero = 0;
    for item in newArr:
        if item == "0": 
            zero+=1
        elif item.startswith("-"):
            minusNumber+=1
        else:
            plusNumbers+=1
        
    
    resultZero = zero/arrSize;
    resultPlus = plusNumbers/arrSize;
    resultMinus = minusNumber/arrSize;
    
    print(f"\n {float(resultZero)} {float(resultPlus)} {float(resultMinus)}")
    return;


plusMinus(array)