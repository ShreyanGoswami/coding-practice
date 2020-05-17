
def kthsmallestelement(arr, k):
    maxValue = max(arr)
    temp = [0] * (maxValue+1)
    toFind = k
    for x in arr:
        temp[x] += 1
    for i in range(0, len(temp)):
        if temp[i] > 0:
            toFind -= temp[i]
        if toFind <= 0:
            return i

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != '':
            inp = inp.split(' ')
            inp = [int(i) for i in inp]
            k = int(input())
            count = kthsmallestelement(inp, k)
            print(count)

main()