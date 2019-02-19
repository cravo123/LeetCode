class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        J = set(J)
        
        res = sum(1 if c in J else 0 for c in S)
        
        return res