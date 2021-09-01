from typing import List
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for (x, y) in points:
            print(x)
        distance = [(sqrt(x ** 2 + y ** 2), [x, y]) for (x, y) in points]
        distance.sort(key=lambda x: x[0])
        res = []
        for d in range(k):
            res.append(distance[d][1])
        return res


if __name__ == "__main__":
    s = Solution()
    points = [[1, 3], [-2, 2]]
    k = 1
    print(s.kClosest(points, k))
