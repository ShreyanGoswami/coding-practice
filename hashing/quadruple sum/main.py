# Incomplete


class Pair:
    def __init__(self, a, b):
        self.first = a
        self.second = b


def findQuads(arr, n, k):
    d = {}
    res = []
    for i in range(n - 1):
        for j in range(i, n):
            sumOfPair = arr[i] + arr[j]
            try:
                d[sumOfPair].append(Pair(i, j))
            except KeyError:
                d[sumOfPair] = [Pair(i, j)]
    for key, value in d.items():
        if k - key in d.keys():
            pair1 = value
            pair2 = d[k - key]
            for p1 in pair1:
                for p2 in pair2:
                    if p1.first != p2.first and p1.second != p2.second:
                        res.append([p1.first, p1.second, p2.first, p2.second])
    return res


if __name__ == "__main__":
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n, k = l[0], l[1]
        arr = list(map(stoi, inp().strip().split()))
        res = findQuads(arr, n, k)
        print(res)
