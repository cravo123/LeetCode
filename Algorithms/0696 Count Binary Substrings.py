class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        prev = curr = 0 # count
        curr_v = s[0]
        
        res = 0
        
        for c in s:
            if c == curr_v:
                curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1
                curr_v = c
        
        res += min(prev, curr)
        
        return res