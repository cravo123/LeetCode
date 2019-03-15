# Solution 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        q = [1]
        
        idx = 0
        
        while idx < numRows:
            res.append(q[::])
            tmp = []
            for a, b in zip([0] + q, q + [0]):
                tmp.append(a + b)
            q = tmp
            idx += 1
        return res

# Solution 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        q = []
        
        for i in range(1, numRows + 1):
            tmp = [1 for _ in range(i)]
            
            left = 1
            while left < i - 1:
                tmp[left] = q[left - 1] + q[left]
                left += 1
            q = tmp
            res.append(q[::])
        return res