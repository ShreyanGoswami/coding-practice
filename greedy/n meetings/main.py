# There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) 
# where S[i] is start time of meeting i and F[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room?

def scheduleMeeting(arr, n):
    d = {}
    for i in range(n):
        d[arr[i]] = i
    arr.sort(key = lambda x : x[0])
    arr.sort(key = lambda x : x[1])
    res = []
    currTime = 0
    for i in range(0, n):
        if currTime < arr[i][0]:
            res.append(d[arr[i]] + 1)
            currTime = arr[i][1]
    return res
    
if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr1 = list(map(stoi, inp().strip().split()))
        arr2 = list(map(stoi, inp().strip().split()))
        arr = list(zip(arr1, arr2))
        res = scheduleMeeting(arr, n)
        print(" ".join(itos(x) for x in res))