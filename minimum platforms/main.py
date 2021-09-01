def minimumPlatforms(times, n):
    arr = []
    for i in range(n):
        arr.append([1 if times[i][0] <= x <= times[i][1] else 0 for x in range(2360)])

    maxValue = 0
    for i in range(1, n):
        for j in range(0, 2359):
            arr[i][j] += arr[i - 1][j]
            if arr[i][j] > maxValue:
                maxValue = arr[i][j]
    return maxValue


if __name__ == "__main__":
    stoi = int
    inp = input
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        startTimes = list(map(stoi, inp().strip().split()))
        endTimes = list(map(stoi, inp().strip().split()))
        times = list(zip(startTimes, endTimes))
        print(minimumPlatforms(times, n))
