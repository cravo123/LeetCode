# Solution 1, try to find middle x, and then prove it right
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:        
        if not points:
            return True
        d = set((x, y) for x, y in points)
        
        # determine x_mid first
        xs = list(set([x for x, _ in points]))
        xs.sort()
        
        if len(xs) % 2 == 1:
            mid = xs[len(xs) // 2] * 2
        else:
            mid = xs[len(xs) // 2] + xs[len(xs) // 2 - 1]
        
        for x, y in d:
            if (mid - x, y) not in d:
                return False
        
        return True

# Solution 2, same idea as Solution 1. But use a more elegant way to
# determine middle point candidate
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        target = min(x for x, _ in points) + max(x for x, _ in points)
        
        d = set((x, y) for x, y in points)
        
        for x, y in d:
            if (target - x, y) not in d:
                return False
        return True