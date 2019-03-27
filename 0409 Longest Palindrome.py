import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        d = collections.Counter(s)
        
        res = 2 * sum(v // 2 for v in d.values()) + (1 if any(v % 2 == 1 for v in d.values()) else 0)
        # can be simplified to 
        #res = 2 * sum(v // 2 for v in d.values())
        #res += 1 if res < len(s) else 0
        
        return res