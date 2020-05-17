def findCommon(n1, n2, n3):
    d = {}
    res = []
    for x in n1:
            d[x] = [1, 0, 0]
    for x in n2:
        if x in d.keys():
            v = d[x]
            v[1] = 1
    for x in n3:
        if x in d.keys():
            v = d[x]
            v[2] = 1
    for k,v in d.items():
        if v == [1, 1, 1]:
            res.append(k)
    if len(res) != 0:
        return res
    return [-1]

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n1 = list(map(stoi, inp().strip().split()))
        n2 = list(map(stoi, inp().strip().split()))
        n3 = list(map(stoi, inp().strip().split()))
        res = findCommon(n1, n2, n3)
        print(" ".join(str(x) for x in res))