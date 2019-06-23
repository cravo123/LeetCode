# Solution 1, simulation
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        path = [1]
        
        for _ in range(numRows):
            res.append(path[::])
            
            left = path + [0]
            right = [0] + path
            
            path = [l + r for l, r in zip(left, right)]
        
        return res

# Solution 2, simulation, O(n) memory
# Add 1 at index i for row i (starting from 0)
# Then populate backward to generate new row vals
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        path = [0 for _ in range(numRows)]
        res = []
        
        for i in range(numRows):
            path[i] = 1
            for j in range(i - 1, 0, -1):
                path[j] += path[j - 1]
            res.append(path[:(i + 1)][::])
        
        return res