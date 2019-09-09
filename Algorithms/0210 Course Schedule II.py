import collections

# Solution 1, indegree count
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        d = collections.defaultdict(set)
        
        for curr, prev in prerequisites:
            d[curr].add(prev)
        
        res = []
        q = collections.deque()
        
        for i in range(n):
            if len(d[i]) == 0:
                q.append(i)
                res.append(i)
        seen = set(q)
        
        while q:
            p = q.pop()
            
            for i in range(n):
                d[i].discard(p)
                if i not in seen and len(d[i]) == 0:
                    q.append(i)
                    res.append(i)
                    seen.add(i)
        return res if len(res) == n else []

# Solution 2, DFS mark node as 1, -1, 0
class Solution(object):
    def dfs(self, idx, d, seen, res):
        if seen[idx] == -1:
            return False
        if seen[idx] == 1:
            return True
        seen[idx] = -1
        
        for x in d[idx]:
            if not self.dfs(x, d, seen, res):
                return False
        seen[idx] = 1
        res.append(idx)
        
        return True
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        
        d = collections.defaultdict(set)
        
        for curr, prev in prerequisites:
            d[curr].add(prev)
        
        res = []
        
        seen = {i:0 for i in range(n)}
        
        for i in range(n):
            if not self.dfs(i, d, seen, res):
                return []
        
        return res