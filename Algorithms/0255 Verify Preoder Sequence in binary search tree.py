import bisect

# Solution 1, linear scanning, maintain max_low
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        q = []
        low = float('-inf')
        
        for v in preorder:
            if v < low:
                return False
            while q and q[-1] < v:
                low = max(q.pop(), low)
            q.append(v)
        return True

# Solution 2, binary search
class Solution:
    def dfs(self, s, low, up):
        if not s:
            return True
        if s[0] <= low or s[0] >= up:
            return False
        if len(s) == 0:
            return True
        
        idx = bisect.bisect_left(s, s[0], lo=1)
        
        return self.dfs(s[1:idx], low, s[0]) and self.dfs(s[idx:], s[0], up)
        
        
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.dfs(preorder, float('-inf'), float('inf'))

# Solution 2.1 similar idea
class Solution:
    def dfs(self, s, low, up, left, right):
        if left > right:
            return True
        if s[left] <= low or s[left] >= up:
            return False
        if left == right:
            return True
        
        idx = bisect.bisect_left(s, s[left], lo=left + 1)
        
        return self.dfs(s, low, s[left], left + 1, idx - 1) and self.dfs(s, s[left], up, idx, right)
        
        
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.dfs(preorder, float('-inf'), float('inf'), 0, len(preorder) - 1)