# Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
# 0 : Empty cell
# 1 : Cells have fresh oranges
# 2 : Cells have rotten oranges

# So, we have to determine what is the minimum time required to rot all oranges. 
# A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
# If it is impossible to rot every orange then simply return -1.

def findTime(arr, rowSize, colSize):
    time = 0
    rotList = [[-1,-1]]

    while True:
        if len(rotList) == 0:
            break
        elif rotList[0] == [-1,-1]:
            rotList.pop()
        else:
            while len(rotList) != 0:
                toRot = rotList.pop()
                toRotI, toRotJ = toRot[0], toRot[1]
                arr[toRotI][toRotJ] = 2
        
        for i in range(rowSize):
            for j in range(colSize):
                if arr[i][j] == 2:
                    if i > 0 and arr[i-1][j] != 2 and arr[i-1][j] != 0:
                        rotList.append([i-1, j])
                    if j > 0 and arr[i][j-1] != 2 and arr[i][j-1] != 0:
                        rotList.append([i, j - 1])
                    if i < n - 1 and arr[i+1][j] != 2 and arr[i+1][j] != 0:
                        rotList.append([i+1, j])
                    if j < m - 1 and arr[i][j+1] != 2 and arr[i][j+1] != 0:
                        rotList.append([i, j+1])
        time += 1
    
    for i in range(rowSize):
            for j in range(colSize):
                if arr[i][j] == 1:
                    return -1
    return time - 1



if __name__ == '__main__':
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n, m = l[0], l[1]
        arr = []
        l = list(map(stoi, inp().strip().split()))
        start = 0
        end = m
        for i in range(n):
            arr.append(l[start:end])
            start = start + m
            end += m
        print(findTime(arr, n, m))