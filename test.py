MIN_SIZE = 1
MAX_SIZE = 100000


demoLogs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
demoThreshold = 2

def processLog(logs, threshold):
    transactions = {}
    output = []
    size = len(logs)
    if(threshold < MIN_SIZE or threshold > size):
        return
    if(size < MIN_SIZE or size > MAX_SIZE):
        return
    for log in logs:
        i = 1
        currentUsers = []
        currentLog = log.split(' ') 
        for item in currentLog:
            if(not item.isnumeric()):
                isError = 1
                print(f"Invalid character in item ${item}!\nitem should be in range ascii['0'-'9']")
                quit()
                
            if(item[0] == "0"):
                print(f"Invalid character in item ${item}!\nItem shouldn't start with 0")
                quit()
            if(len(item) <0 or len(item) >9):
                print(f"Invalid item - {item} - item length shouldn't exceed 9 or be lower than 0")
            if(item in currentUsers):
                break
            if i == len(currentLog) :
                break
            if str(item) in transactions:
                transactions[str(item)] += 1
            else:
                transactions[str(item)] = 1
            currentUsers.append(item)        
            i+=1
    for item in transactions:
        if(transactions[item] >= 2):
            output.append(item)
    return output

transactions = processLog(demoLogs,demoThreshold)
print(transactions)