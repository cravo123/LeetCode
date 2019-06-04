import collections

# Solution 1, simulation
# Uncommon means that word only occurs once in A + B
class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        da, db = map(collections.Counter, (A.split(), B.split()))
        d = da + db
        
        res = [word for word, cnt in d.items() if cnt == 1]
        
        return res