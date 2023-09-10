height = [1,8,2,6,2,5,4,1,7,9]


def maxArea(arr):
    king1 = 0
    king2 = 0
    for i in range(len(arr)):
        if arr[i] > king1:
            king1 = arr[i]
    for i in range(len(arr)):
        if arr[i] > king2 and arr[i] < king1:
            king2 = arr[i]
    return king2 * king2
print(maxArea(height))