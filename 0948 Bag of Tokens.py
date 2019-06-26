# Solution 1, greedy
# Use cheapest token to gain point, otherwise Use most expensive token to gain power
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        
        i, j = 0, len(tokens) - 1
        
        pts = res = 0
        
        while i <= j:
            if P >= tokens[i]:
                P -= tokens[i]
                i += 1
                pts += 1
            elif pts > 0:
                P += tokens[j]
                j -= 1
                pts -= 1
            else:
                break
            res = max(res, pts)
        
        return res