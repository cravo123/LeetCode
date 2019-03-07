class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        res = 0
        
        m, n = len(g), len(s)
        i = j = 0
        
        while i < m and j < n:
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res