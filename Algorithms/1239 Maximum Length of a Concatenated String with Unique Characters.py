# Solution 1, brute-force
# Save all valid combinations when iterating
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [set()]
        
        for s in arr:
            if len(set(s)) < len(s):
                continue
            s = set(s)
            for s_old in res:
                if s_old & s:
                    continue
                res.append(s_old | s)
        
        return max(len(x) for x in res)