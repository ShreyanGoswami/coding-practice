from collections import deque


def printSpiral(root):
    # Code here
    if root is None:
        return
    q = deque()
    print(root.data, end=" ")
    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right)
    isLeftToRight = True
    while len(q) > 0:
        n = len(q)
        temp = deque()
        for _ in range(n):
            curr = q.popleft()
            temp.append(curr)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        while len(temp) != 0:
            curr = temp.popleft() if isLeftToRight else temp.pop()
            print(curr.data, end=" ")
        isLeftToRight = not isLeftToRight
