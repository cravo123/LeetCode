# Solution 1, Stack solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ts = [(p, -(target - p) / s) for p, s in zip(position, speed)]
        ts.sort()
        q = []
        
        for _, t in ts:
            t = -t
            while q and q[-1] <= t:
                q.pop()
            q.append(t)
        
        return len(q)

# Solution 2, similar idea,
# but traverse ts backward, we don't need those many stack pop any more
