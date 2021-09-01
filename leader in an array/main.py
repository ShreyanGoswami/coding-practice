# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements to its right side.
# Also, the rightmost element is always a leader.


def findLeaders(arr, n):
    temp = arr[::-1]
    res = []
    maxTillNow = -1
    for x in temp:
        if x >= maxTillNow:
            res.append(x)
            maxTillNow = x
    return res[::-1]


if __name__ == "__main__":
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        l = list(map(stoi, inp().strip().split()))
        res = findLeaders(l, n)
        print(" ".join(itos(x) for x in res))
