'''
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
The result is going to be very large, hence return the result in the form of a string.
'''

def isGreater(a, b, strFunc, intFunc):
    stra = strFunc(a)
    strb = strFunc(b)
    first = stra + strb
    second = strb + stra
    if intFunc(first) > intFunc(second):
        return True
    return False

def getLargestNumber(arr, n, strFunc, intFunc):
    res = []
    for i in range(n - 1):
       for j in range(i + 1, n):
           if isGreater(arr[i], arr[j], strFunc, intFunc) == False:
               temp = arr[i]
               arr[i] = arr[j]
               arr[j] = temp
    return arr

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        res = getLargestNumber(arr, n, itos, stoi)
        print(''.join(itos(x) for x in res))