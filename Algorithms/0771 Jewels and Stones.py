import collections

# Solution 1, hash-table
class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        J = set(J)
        
        res = sum(1 if c in J else 0 for c in S)
        
        return res

# Solution 1.1, hash-table using collections.Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        d = collections.Counter(S)
        return sum(v for c, v in d.items() if c in J)