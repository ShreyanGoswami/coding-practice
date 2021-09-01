def findIslands(a, n, m):
    def dfs(a, row, col, n, m):
        a[row][col] = 2
        if row - 1 >= 0 and a[row - 1][col] == 1:
            dfs(a, row - 1, col, n, m)
        if row + 1 != n and a[row + 1][col] == 1:
            dfs(a, row + 1, col, n, m)
        if col - 1 >= 0 and a[row][col - 1] == 1:
            dfs(a, row, col - 1, n, m)
        if col + 1 != m and a[row][col + 1] == 1:
            dfs(a, row, col + 1, n, m)
        if row + 1 != n and col + 1 != m and a[row + 1][col + 1] == 1:
            dfs(a, row + 1, col + 1, n, m)
        if row + 1 != n and col - 1 >= 0 and a[row + 1][col - 1] == 1:
            dfs(a, row + 1, col - 1, n, m)
        if row - 1 >= 0 and col + 1 < m and a[row - 1][col + 1] == 1:
            dfs(a, row - 1, col + 1, n, m)

    islands = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                islands += 1
                dfs(a, i, j, n, m)
    return islands


if __name__ == "__main__":
    # a = [[1, 1, 0], [0, 0, 1], [1, 0, 1]]
    # print(findIslands(a, 3, 3))
    # a = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    # print(findIslands(a, 4, 4))
    a = [
        [1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1],
    ]
    print(findIslands(a, 4, 7))
