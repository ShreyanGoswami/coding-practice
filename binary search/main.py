def bin_search(arr, left, high, key):
    import math

    left = 0
    n = len(arr)
    right = n - 1
    while left < right:
        mid = math.ceil((left + right) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
            if right >= 0 and arr[right] == key:
                return right
        else:
            left = mid + 1
            if left < n and arr[left] == key:
                return left
    return -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(bin_search(arr, 0, 0, k))
