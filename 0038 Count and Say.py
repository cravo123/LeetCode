# Solution 1, simulation
# Similar to Run Length Encoding
class Solution:
    def count(self, q):
        res = []
        curr = q[0]
        cnt = 0

        for c in q:
            if c == curr:
                cnt += 1
            else:
                res.extend([cnt, curr])
                curr = c
                cnt = 1
        res.extend([cnt, curr])
        
        return res
        
    def countAndSay(self, n: int) -> str:
        q = [1]
        
        for _ in range(1, n):
            q = self.count(q)
        
        res = ''.join(str(x) for x in q)
        
        return res