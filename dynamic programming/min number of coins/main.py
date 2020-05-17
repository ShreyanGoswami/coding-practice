def findMinimumNumberOfNotes(n):
    c = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    res = []
    for i in range(0, n + 1):
        res.append([])
    res[0] = []
    c = [x for x in c if x <= n]
    for x in c:
        res[x] = [x]
    
    for i in range(1, n+1):
        minLen = -1
        if len(res[i]) != 1:
            maxValueToCut = 0
            for x in c:
                if x > maxValueToCut and x <= i:
                    maxValueToCut = x
            res[i] = [x for x in res[i-maxValueToCut]]
            res[i].append(maxValueToCut)
    return res[n]

if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        n = int(input())
        res = findMinimumNumberOfNotes(n)
        #sort in descending order
        res.sort(reverse=true)
        print(" ".join(str(x) for x in res))
