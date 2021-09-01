# Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2.
# For the elements not present in A2, append them at last in sorted order.
# It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.


def relativeSort(arr, order):
    d = {}
    sortedArr = []
    for x in arr:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in order:
        for i in range(0, d[x]):
            sortedArr.append(x)
        del d[x]
    temp = []
    for k, v in d.items():
        for i in range(0, v):
            temp.append(k)
    temp.sort()
    for x in temp:
        sortedArr.append(x)
    return sortedArr


def main():
    t = int(input())
    for i in range(0, t):
        l = input().split(" ")
        n, m = int(l[0]), int(l[1])
        inp = input().strip()
        order = input().strip().split(" ")
        if inp is not None and inp != "":
            inp = inp.split(" ")
            inp = [int(i) for i in inp]
            order = [int(i) for i in order]
            inp = relativeSort(inp, order)
            output = " ".join([str(elem) for elem in inp])
            print(output)


main()
