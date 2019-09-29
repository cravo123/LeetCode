import collections

# Solution 1, set
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.Counter(arr).values()
        
        return len(d) == len(set(d))
        