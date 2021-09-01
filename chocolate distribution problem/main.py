# Given an array A of positive integers of size N, where each value represents number of chocolates in a packet.
# Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
# 1. Each student gets one packet.
# 2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum.
def minimumChocolates(n, arr, k):
    arr.sort()
    start = 0
    end = k - 1
    diff = -1
    while end < n:
        d = arr[end] - arr[start]
        if diff == -1:
            diff = d
        elif diff > d:
            diff = d
        start += 1
        end += 1
    return diff


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        k = stoi(inp())
        print(minimumChocolates(n, arr, k))
