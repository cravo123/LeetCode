import collections

# Similar to LC 0438 Find All Anagrams in a String

# Solution 1, sliding-window solution
# When we see "permutation" or order doesn't matter, we should always think of
# using dict to cache temporary results 
# we are comparing whole Counter, which is inefficient
class Solution:
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

# Solution 1.1, sliding-window better solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = collections.Counter(s1)
        need = len(s1)
        n = len(s1)
        
        curr = collections.Counter()
        j = 0
        for i, c in enumerate(s2):
            curr[c] += 1
            if curr[c] <= d[c]:
                need -= 1
            
            if i - j + 1 > n:
                v = s2[j]
                curr[v] -= 1
                if curr[v] < d[v]:
                    need += 1
                j += 1
            
            if need == 0:
                return True
        
        return False