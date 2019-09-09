class Solution:
    def generate(self, num: str):
        if len(num) == 1:
            return [num]
        
        if not num or num[0] == num[-1] == '0':
            return []
        
        if num[-1] == '0':
            return [num]
        
        if num[0] == '0':
            return [num[0] + '.' + num[1:]]
        
        res = [num]
        for i in range(1, len(num)):
            res.append(num[:i] + '.' + num[i:])
        
        return res
        
    def ambiguousCoordinates(self, S: str) -> List[str]:
        
        res = []
        S = S[1:-1]
        n = len(S)
        
        for i in range(1, n):
            left = S[:i]
            right = S[i:]
            
            for a in self.generate(left):
                for b in self.generate(right):
                    res.append('(%s, %s)' % (a, b))
        
        return res