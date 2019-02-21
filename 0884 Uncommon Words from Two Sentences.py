class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        da, db = map(collections.Counter, (A.split(), B.split()))
        d = da + db
        
        res = [x for x in d if d[x] == 1]
        return res
