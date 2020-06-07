from typing import List
class Solution:
    
    def findLocation(self, people, index):
        return people[index][1]
        
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0],x[1]))
        for i,p in enumerate(people):
            toMove = self.findLocation(people, i)
            people.insert(toMove, people.pop(i))
        return people

if __name__ == "__main__":
    s = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    # people = [[5,1],[5,0],[4,1]]
    print(s.reconstructQueue(people))