def findSum(arr, sum):
    found = False
    for i in range(0, len(arr)):
        startIndex = i
        endIndex = -1
        temp = sum
        if arr[i] > temp:
            continue
        temp = temp - arr[i]
        if temp == 0:
            endIndex = i
        else:
            for j in range(i + 1, len(arr)):
                temp = temp - arr[j]
                if temp < 0:
                    break
                if temp == 0:
                    endIndex = j
                    break
        if endIndex != -1:
            print(startIndex + 1, endIndex + 1)
            found = True
            break
    if found == False:
        print(-1)


def findSumOptimized(arr, sum):
    found = False
    startIndex = 0
    endIndex = 0
    currSum = arr[startIndex]
    while True:
        if currSum == sum:
            print(startIndex + 1, endIndex + 1)
            break
        if currSum < sum:
            endIndex = endIndex + 1
            if endIndex == len(arr):
                print(-1)
                break
            currSum = currSum + arr[endIndex]
        if currSum > sum:
            currSum = currSum - arr[startIndex]
            startIndex = startIndex + 1


def main():
    t = int(input())
    for i in range(0, t):
        l = input().split(" ")
        n, s = int(l[0]), int(l[1])
        inp = input().strip()
        if inp is not None and inp != "":
            inp = inp.split(" ")
            inp = [int(i) for i in inp]
            findSumOptimized(inp, s)


main()
