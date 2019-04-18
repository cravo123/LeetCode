class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        power = P
        res = points = 0
        
        tokens.sort()
        i, j = 0, len(tokens) - 1
        
        while i <= j and (power >= tokens[i] or points > 0):
            if power >= tokens[i]:
                power -= tokens[i]
                points += 1
                i += 1
            elif points > 0:
                points -= 1
                power += tokens[j]
                j -= 1
            
            res = max(res, points)
        
        return res