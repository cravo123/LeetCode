# Solution 1, simulation
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        q = [0 for _ in range(rowIndex + 1)]
        
        for i in range(rowIndex + 1):
            q[i] = 1
            
            for j in range(i - 1, 0, -1):
                q[j] += q[j - 1]
        
        return q