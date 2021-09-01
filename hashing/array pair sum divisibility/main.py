def areAllPairsDivisible(arr, n, k):
    if n % 2 == 1:
        return False
    arr = [x % k for x in arr]
    d = {}
    for x in arr:
        try:
            d[x] += 1
        except KeyError:
            d[x] = 1

    for num, count in d.items():
        if num == 0:
            if count % 2 != 0:
                return False
            continue

        toFind = k - num
        if toFind == num:
            if count % 2 != 0:
                return False
        else:
            if toFind not in d.keys():
                return False
            if count != d[toFind]:
                return False
    return True


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        k = stoi(inp())
        print(areAllPairsDivisible(arr, n, k))
