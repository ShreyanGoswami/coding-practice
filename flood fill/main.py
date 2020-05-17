from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalCol = image[sr][sc]
        q = []
        q.append([sr,sc])
        
        while len(q) != 0:
            row, col = q.pop()
            image[row][col] = newColor
            if row != 0:
                if image[row-1][sc] == originalCol: q.append([row-1, col])
            if row != len(image) - 1:
                if image[row+1][col] == originalCol: q.append([row+1, col])
            if col != 0:
                if image[row][col-1] == originalCol and image[row][col-1] != newColor: q.append([row, col-1])
            if col != len(image[0]) - 1:
                if image[row][col+1] == originalCol and image[row][col+1] != newColor: q.append([row, col+1])
        
        return image

image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
print(floodFill(image, sr,sc, newColor))