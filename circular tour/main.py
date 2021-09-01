# Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
# 1. The amount of petrol that every petrol pump has.
# 2. Distance from that petrol pump to the next petrol pump.

# Your task is to complete the function tour() which returns an integer denoting the first point from where a truck will be able to complete the circle
# (The truck will stop at each petrol pump and it has infinite capacity).

# Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.


def reset(end, n):
    if end >= n:
        return 0
    return end


def tour(lis, n):
    if len(lis) == 1:
        return 0
    diff = [p[0] - p[1] for p in lis]
    start = 0
    end = n - 1
    isReset = False
    while diff[start] < 0:
        start += 1
        if start == n:
            return -1
        end += 1
        if end == n:
            end = 0

    temp = start
    s = 0
    steps = 0
    while True:
        s += diff[temp]
        temp += 1
        steps += 1

        if s < 0 and isReset == True:
            return -1

        if temp == n:
            temp = 0
            isReset = True

        if s < 0:
            end = (end + steps) % n
            s = 0
            start = temp
            steps = 0

        if temp == end and s + diff[temp] >= 0:
            return start
        elif temp == end and s + diff[temp] < 0:
            return -1

    return -1


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        inp = list(map(stoi, inp().strip().split()))
        p = inp[::2]
        d = inp[1::2]
        arr = list(zip(p, d))
        print(tour(arr, n))
