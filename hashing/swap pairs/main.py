# Given two arrays of integers, write a program to check if a pair of values (one value from each array) exists
# such that swapping the elements of the pair will make the sum of two arrays equal.
def doesPairExist(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff = abs(sum1 - sum2)
    d = {}
    for x in arr2:
        d[x] = 1
    for x in arr1:
        if abs(diff - x) in d.keys():
            return 1
    return -1


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n1, n2 = l[0], l[1]
        arr1 = list(map(stoi, inp().strip().split()))
        arr2 = list(map(stoi, inp().strip().split()))
        print(doesPairExist(arr1, arr2))
