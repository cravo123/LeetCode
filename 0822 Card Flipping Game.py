# Solution 1, hashtable + sort
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cannot = set([i for i, j in zip(fronts, backs) if i == j])
        
        cans = set(fronts + backs)
        
        # actually no need to sort
        # can do O(n) traverse to find the minimum
        for c in sorted(cans):
            if c not in cannot:
                return c
        
        return 0

# Solution 2, without sorting
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cannot = set([i for i, j in zip(fronts, backs) if i == j])
        
        cans = set(fronts + backs)
        
        res = float('inf')
        
        for i in range(len(fronts)):
            if fronts[i] not in cannot:
                res = min(res, fronts[i])
            if backs[i] not in cannot:
                res = min(res, backs[i])
                
        
        return res if res < float('inf') else 0