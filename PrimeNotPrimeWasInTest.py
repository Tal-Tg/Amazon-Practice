
arr = ["zld 93 12","fp kindle book", "10a echo show", "17g 12 25 6", "ab1 kindle book", "125 echo dot second generation"]


def sortOrders(arr):
    prime=[]
    nonPrime=[]
    for i in arr:
        newArr=list(i.split())
        if newArr[1].isnumeric():
            nonPrime.append(newArr) 
        else:
            prime.append(newArr)
    for i in range(len(prime)):
        newString=' '.join(prime[i][1:])
        key=prime[i][0]
        prime[i]=[newString , key]
        print(prime[i])
    prime.sort()
    for i in range(len(prime)):
        prime[i]=prime[i][1]+" "+prime[i][0]
    for i in range(len(nonPrime)):
        nonPrime[i]=' '.join(nonPrime[i])
    return prime+nonPrime


# def sortOrders(arr):
#     arrPrime=[]
#     nonArrPrime=[]
    
#     for i in arr:
#         newArr=list(i.split())
#         if newArr[1].isnumeric():
#             nonArrPrime.append(newArr) 
#         else:
#             arrPrime.append(newArr)
#     for i in range(len(arrPrime)):
#         newString=' '.join(arrPrime[i][1:])
#         key=arrPrime[i][0]
#         arrPrime[i]=[newString, key]
#     arrPrime.sort()
    
#     for i in range(len(arrPrime)):
#         arrPrime[i]=arrPrime[i][1]+" "+arrPrime[i][0]
#     for i in range(len(nonArrPrime)):
#         nonArrPrime[i]=' '.join(nonArrPrime[i])
#     return nonArrPrime + nonArrPrime

print(sortOrders(arr))