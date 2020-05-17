# The cost of stock on each day is given in an array A[] of size N. 
# Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

def findDays(arr, n):
    res = []
    start = 0
    while start != n - 1:
        if arr[start] < arr[start + 1]:
            buyStart = start
            start += 1
            isSellFound = True
            if start != n-1:
                while arr[start] < arr[start + 1]:
                    start += 1
                    if start == n-1:
                        if arr[start] < arr[start - 1]:
                            isSellFound = False
                        break
                if isSellFound == True:
                    res.append([buyStart, start])
            else:
                if arr[start] > arr[start - 1]:
                    res.append([start - 1, start])
                break
        else:
            start += 1
    return res

if __name__ == '__main__':
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        res = findDays(arr, n)
        if len(res) > 0:
            op = ''
            for x in res:
                op = op + '(' + str(x[0]) + ' ' + str(x[1]) + ') '
            print(op)
        else:
            print('No Profit')