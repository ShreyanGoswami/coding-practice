def isCyclic(n, graph):
    # Code here
    white = set()
    for x in range(n):
        white.add(x)
    grey = set()
    black = set()

    def changeColour(intialColour, finalColour, i):
        try:
            intialColour.remove(i)
            finalColour.add(i)
        except KeyError:
            pass

    def dfs(white, grey, black, node, graph):
        if node in graph:
            for v in graph[node]:
                if v in grey:
                    return 1
                if v in white:
                    changeColour(white, grey, v)
                    isCyclePresent = dfs(white, grey, black, v, graph)
                    if isCyclePresent == 1:
                        return 1
                    changeColour(grey, black, v)
            changeColour(grey, black, node)
            return 0
        changeColour(grey, black, node)
        return 0

    for i in range(n):
        if i in graph and i in white:
            white.remove(i)
            grey.add(i)
            isCyclic = dfs(white, grey, black, i, graph)
            if isCyclic == 1:
                return 1
    return 0


if __name__ == "__main__":
    graph = {0: [1, 0]}
    assert isCyclic(2, graph) == 1
    graph = {0: [1], 1: [2], 2: [3]}
    assert isCyclic(4, graph) == 0
    graph = {0: [1], 2: [3], 3: [2]}
    assert isCyclic(4, graph) == 1
    graph = {6: [21], 17: [12], 2: [11], 9: [11]}
    assert isCyclic(29, graph) == 0
    graph = {
        12: [28],
        67: [17],
        0: [26],
        30: [11],
        38: [85],
        57: [60],
        57: [15],
        75: [31],
        65: [80],
        75: [19],
        68: [67],
        73: [84],
        63: [86],
    }
    assert isCyclic(88, graph) == 0
