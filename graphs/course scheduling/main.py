from typing import List


class Solution:
    def getNeighbours(self, curr, graph):
        try:
            return graph[curr]
        except KeyError:
            return []

    def colourNode(self, curr, initial, final):
        try:
            initial.remove(curr)
            final.add(curr)
        except KeyError:
            pass

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = set(range(numCourses))
        grey = set()
        black = set()

        if len(prerequisites) == 0:
            return True

        def traverse(curr, graph, white, grey, black) -> bool:
            if curr in grey:
                return False
            self.colourNode(curr, white, grey)
            neighbours = self.getNeighbours(curr, graph)
            for neighbour in neighbours:
                if neighbour not in black:
                    res = traverse(neighbour, graph, white, grey, black)
                    if res == False:
                        return False
            self.colourNode(curr, grey, black)
            return True

        graph = {}
        for x in prerequisites:
            try:
                graph[x[0]].append(x[1])
            except KeyError:
                graph[x[0]] = [x[1]]

        for i in range(numCourses):
            if i not in black:
                if traverse(i, graph, white, grey, black) == False:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    numOfCourses = 4
    graph = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    print(s.canFinish(numOfCourses, graph))
