import collections

# Sliding-window solution
# When we see "permutation" or order doesn't matter, we should always think of
# using dict to cache temporary results 

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        d = collections.Counter(s1)
        
        curr = collections.Counter()
        
        for i, c in enumerate(s2):
            curr[c] += 1
            if i >= n:
                v = s2[i - n]
                curr[v] -= 1
                if curr[v] == 0:
                    del curr[v]
            if curr == d:
                return True
        
        return False