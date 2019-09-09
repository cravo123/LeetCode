import collections

# Solution 1, simulation
class Solution:
    def checkRecord(self, s: str) -> bool:
        d = collections.Counter(s)
        
        return 'LLL' not in s and d['A'] < 2