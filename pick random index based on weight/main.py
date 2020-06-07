import random
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        self.s = sum(w)
        self.l = len(w)
        self.prefixSum = [w[0]]
        self.buckets = [[0, w[0]]]
        index = 1
        for x in w[1:]:
            self.prefixSum.append(self.prefixSum[index-1] + x)
            self.buckets.append([self.prefixSum[index-1], self.prefixSum[index]])
            index += 1
        
    def pickIndex(self) -> int:
        randomNumber = random.randint(0,self.s)
        # print('Adding number ', randomNumber)
        return self.findBucket(randomNumber)
    
    def findBucket(self, randomNumber: int) -> int:
        start = 0
        end = self.l
        if end == 1:
            return 0
        while start <= end:
            mid = (start + end) >> 1
            if mid == 0:
                return 0
            if self.buckets[mid][0] < randomNumber <= self.buckets[mid][1]:
                return mid
            elif randomNumber > self.buckets[mid][1]:
                start = mid + 1
            else:
                end = mid - 1

if __name__ == "__main__":
    obj = Solution([1,3])
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())