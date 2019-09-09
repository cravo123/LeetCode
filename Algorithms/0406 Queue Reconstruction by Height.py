from heapq import *

# Solution 1, this is essentially O(n**n) complexity since we need to insert
# in the middle of an array
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = [[-h, k] for h, k in people]
        heapify(people)
        
        q = []
        
        while people:
            h, idx = heappop(people)
            h = -h
            q.insert(idx, [h, idx])
        
        return q

# Solution 2, similar idea but better implementation
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        
        res = []        
        for h, k in people:
            res.insert(k, [h, k])
            
        return res