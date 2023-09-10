a = [[1, 1, 0], 
    [1, 1, 0],
    [0 ,0 , 1]]

def countGroups(related):
    count = 0
    length = len(related)
    related = convertToArray(related)
    
    for indx in range(length):
        if related[indx][indx] == 1:
            count +=1
            dfs(indx, length, related)
    return count

def dfs(idx, length,matrix):
    if matrix[idx][idx] == 0:
        return 
    for i in range(length):
        if matrix[idx][i]==1:
            matrix[idx][i]=0
            dfs(i,length,matrix)
            
            
def convertToArray(s):
    result = []
    for char in s:
        result.append([int(x) for x in char])
    return result    
            
            
print(countGroups(a))