# Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller 
# and all right elements to it are greater than it.
# Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

def findEleOptimized(arr, n):
    index = 1
    maxLeft = arr[0]
    minRight = min(arr[2:])
    while index < n-1:
        if arr[index] >= maxLeft and arr[index] <= minRight:
            return arr[index]
        else:
            if arr[index] < maxLeft:
                index += 1
                if index == n - 1:
                    return -1
                if arr[index] == minRight:
                    minRight = min(arr[index+1: ])
                continue
            if arr[index] > minRight and arr[index] >= maxLeft:
                maxLeft = arr[index]
                index += 1
                if index == n - 1:
                    return -1
                if arr[index] == minRight:
                    minRight = min(arr[index+1: ])
            elif arr[index] < maxLeft and arr[index] > minRight:
                index += 1
                if index == n - 1:
                    return -1
                if arr[index] == minRight:
                    minRight = min(arr[index+1: ])
    return -1

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        print(findEleOptimized(arr, n))