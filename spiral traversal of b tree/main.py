def printSpiral(root):
    # Code here
    if root is None:
        return
    q = deque()
    print(root.data, end=' ')
    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right)
    isLeftToRight = True
    while len(q) > 0:
        n = len(q)
        temp = deque()
        for _ in range(0, n):
            curr = q.popleft()
            temp.append(curr)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        if isLeftToRight == True:
            while len(temp) != 0:
                curr = temp.popleft()
                print(curr.data, end = ' ')
        else:
            while len(temp) != 0:
                curr = temp.pop()
                print(curr.data, end = ' ')
        isLeftToRight = not isLeftToRight
            
     


