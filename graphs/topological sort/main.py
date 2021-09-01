def topoSort(n, graph):
    # Code here
    visited = set()
    res = []

    def topSort(curr, graph, visited, res):
        visited.add(curr)
        if curr in graph:
            for v in graph[curr]:
                if v not in visited:
                    topSort(v, graph, visited, res)
        res.append(curr)

    for v in graph.keys():
        if v not in visited:
            topSort(v, graph, visited, res)

    toAdd = list(set(range(n).difference(set(res))))
    res.extend(toAdd)
    return list(reversed(res))


if __name__ == "__main__":
    g = {1: [3], 2: [3], 4: [0, 1], 5: [0, 2]}
    print(topoSort(6, g))
