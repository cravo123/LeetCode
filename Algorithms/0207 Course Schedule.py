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
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = collections.defaultdict(set)
        
        for curr, prev in prerequisites:
            d[curr].add(prev)
        
        q = collections.deque()
        seen = set()
        for p in range(numCourses):
            if len(d[p]) == 0:
                q.append(p)
                seen.add(p)
        
        while q:
            p = q.popleft()
            
            for x in range(numCourses):
                d[x].discard(p)
                if len(d[x]) == 0 and x not in seen:
                    seen.add(x)
                    q.append(x)
        
        return len(seen) == numCourses

# Solution 3, DFS, detect circle in a graph
class Solution(object):
    def dfs(self, idx, seen, d):
        if seen[idx] == -1:
            return False
        if seen[idx] == 1:
            return True
        seen[idx] = -1
        for j in d[idx]:
            if not self.dfs(j, seen, d):
                return False
        seen[idx] = 1
        return True
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        
        d = collections.defaultdict(set)
        
        for curr, prev in prerequisites:
            d[curr].add(prev)
        
        seen = {i:0 for i in range(n)}
        
        for i in range(n):
            if not self.dfs(i, seen, d):
                return False
        
        return True