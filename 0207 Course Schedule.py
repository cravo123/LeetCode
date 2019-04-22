import collections

# Solution 1, topologic sorting, but not elegant
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(set)
        
        for curr, prev in prerequisites:
            d[curr].add(prev)
        
        curr = set([i for i in range(numCourses) if len(d[i]) == 0])
        seen = set(curr)
        
        while curr:
            t = set()
            
            for i in d:
                d[i] = d[i] - curr
                if len(d[i]) == 0:
                    t.add(i)
            
            for i in t:
                del d[i]
            
            seen = seen | t
            curr = t
        
        return len(seen) == numCourses

# Solution 2, same idea