# Given two unsorted arrays A of size N and B of size M of distinct elements, 
# the task is to find all pairs from both arrays whose sum is equal to X.

def findPairs(arr1, arr2, k):
    d = {}
    res = []
    for x in arr2:
        try:
            d[x] += 1
        except KeyError:
            d[x] = 1
    
    for x in arr1:
        toFind = k - x
        if toFind in d:
            res.append([x, toFind])
    return res

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n1, n2, k = l[0], l[1], l[2]
        arr1 = list(map(stoi, inp().strip().split()))
        arr2 = list(map(stoi, inp().strip().split()))
        res = findPairs(arr1, arr2, k)
        res.sort()
        if len(res) == 0:
            print("-1")
        for i in range(len(res)):
            print(" ".join(itos(p) for p in res[i]),end="")
            if i != len(res) - 1:
                print(",",end=" ")
            else:
                print()