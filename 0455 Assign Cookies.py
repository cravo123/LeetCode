# Solution 1, greedy
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i, m = 0, len(g)
        
        for c in s:
            if i == m:
                break
            if g[i] <= c:
                i += 1
        
        return i