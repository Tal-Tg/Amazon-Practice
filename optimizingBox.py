
arr = [3,7,5,6,2]

def minimalHeaviestSetA(arr):
    arr = sorted(arr)
    target = sum(arr) // 2
    i = len(arr) - 2 
    sum_A = sum(arr[i:])

    while sum_A <= target:
        min_steps = max(1, (target - sum_A) // max(1, arr[i]))
        sum_A += sum(arr[i-min_steps:i])
        i -= min_steps
    return arr[i:]


print(minimalHeaviestSetA(arr))