# Solution 1, DFS
class Solution:
    def dfs(self, idx, d, h):
        if idx not in d and not h[idx]:
            return 0, False
        
        flag = False
        res = 0
        for i in d[idx]:
            status = self.dfs(i, d, h)
            flag = flag or status[1]
            res += status[0]
        
        flag = flag or h[idx]
        if flag:
            res += 2
        
        return res, flag
        
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build tree
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v) # d[parent].add(child)
        
        # Traverse to see if it has apple
        return max(self.dfs(0, d, hasApple)[0] - 2, 0) # -2 here is not intuitive
