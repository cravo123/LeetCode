class Solution:
    def anagramMappings(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        d = {}
        for i, c in enumerate(B):
            d.setdefault(c, i)
        
        P = [d[c] for c in A]
        
        return P