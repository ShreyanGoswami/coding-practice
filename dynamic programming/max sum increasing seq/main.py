# Given an array A of N positive integers. Find the sum of maximum sum increasing subsequence of the given array. 

def findSum(arr):
    sum = 0
    for n in arr:
        sum = sum + n
    return sum

def generateIncreasingSequence(arr, index, seq, maxSum):
    if index == len(arr):
        return 0
    if arr[index] > seq[len(seq) - 1]: #Either add the number to the growing sequence or don't add it
        seq.append(arr[index])
        maxSum1 = maxSum + arr[index] + generateIncreasingSequence(arr,index+1, seq, maxSum)
        seq.pop()
        maxSum2 = maxSum + generateIncreasingSequence(arr, index+1, seq, maxSum)
        if maxSum1 > maxSum2:
            maxSum = maxSum1
        else:
            maxSum = maxSum2
    else:
        maxSum = maxSum + generateIncreasingSequence(arr, index + 1, seq, maxSum)
    return maxSum

def findMax(s,arr,curr):
    max = 0
    for i in range(0,len(arr)):
        if arr[i] < curr:
            if s[i] > max:
                max = s[i]
    return max

def generateIncreasingSequenceOptimized(arr):
    s = []
    for x in arr:
        s.append(x)
    
    for i in range(1, len(arr)):
        s[i]=s[i]+findMax(s[0:i], arr[0:i], arr[i])
    return max(s)

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != '':
            inp = inp.split(' ')
            inp = [int(i) for i in inp]
            print(generateIncreasingSequenceOptimized(inp))

main()