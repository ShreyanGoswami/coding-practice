# Given an array A[] of integers, sort the array according to frequency of elements. 
# That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.
import operator

def sortByFrequency(arr, n):
    d = {}
    for x in arr:
        try:
            d[x] += 1
        except KeyError:
            d[x] = 1
    temp = list(d.items())
    temp = sorted(temp, key = lambda x : (x[0]))
    temp = sorted(temp, key = lambda x : (x[1]), reverse=True)

    res = []
    for x in temp:
        for i in range(0, x[1]):
            res.append(x[0])
    return res

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        arr = sortByFrequency(arr, n)
        print(' '.join(itos(x) for x in arr))