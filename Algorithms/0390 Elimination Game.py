import collections

# Solution 2, simulation
class Solution:
    def lastRemaining(self, n: int) -> int:
        q = collections.deque(range(1, n + 1))
        
        while len(q) > 1:
            tmp = collections.deque()
            
            while q:
                q.popleft()
                
                if q:
                    tmp.appendleft(q.popleft())
            
            q = tmp
        
        return q.pop()