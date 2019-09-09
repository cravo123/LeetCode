import collections

# Solution 1,
class Solution:
    def anagramMappings(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        d = {}
        for i, c in enumerate(B):
            d.setdefault(c, i)
        
        P = [d[c] for c in A]
        
        return P

# Solution 2, follow-up, if there can not be any duplicates in output
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        
        for i, c in enumerate(B):
            d[c].append(i)
        
        res = [d[c].pop() for c in A]
        
        return res
        