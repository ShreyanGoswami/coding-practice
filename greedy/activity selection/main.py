# Given N activities with their start and finish times. 
# Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def convertToPair(value):
    return Pair(value[0], value[1])

def maxNumberOfActivities(arr):
    arr.sort(key = lambda x: x.second)
    maxActivities = 1
    last = arr[0]
    for x in arr[1:]:
        if x.first >= last.second:
            maxActivities += 1
            last = x
    return maxActivities

if __name__ == "__main__":
    inputFunc = input
    intFunc = int
    t = intFunc(inputFunc())
    for i in range(t):
        n = intFunc(inputFunc())
        startTimes = list(map(intFunc, inputFunc().strip().split()))
        endTimes = list(map(intFunc, inputFunc().strip().split()))
        inp = list(map(convertToPair, zip(startTimes, endTimes)))
        print(maxNumberOfActivities(inp))