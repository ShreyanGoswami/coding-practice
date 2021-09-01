def findNonRepeating(arr, n):
    s = set()
    q = []
    res = []
    for x in arr:
        if x not in s:
            if len(q) == 0:
                q.append(x)
                res.append(x)
            else:
                if x in q:
                    # remove x from q
                    q.remove(x)
                    # add to s
                    s.add(x)
                else:
                    # add x to q
                    q.append(x)
                # take the 0th element(if present) from q and add to res else add -1
                if len(q) != 0:
                    res.append(q[0])
                else:
                    res.append("-1")
        else:
            # take the 0the element(if present) from q and add to res else add -1
            if len(q) == 0:
                res.append(-1)
            else:
                res.append(q[0])
    return res


if __name__ == "__main__":
    inp = input
    itos = int
    stoi = str
    t = itos(inp())
    for i in range(t):
        n = itos(inp())
        arr = inp().strip().split()
        res = findNonRepeating(arr, n)
        print(" ".join(x for x in res))
