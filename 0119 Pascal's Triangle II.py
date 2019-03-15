class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        q = [1]
        idx = 0
        
        while idx <= rowIndex:
            tmp = [1 for _ in range(idx + 1)]
            
            i = 1
            while i < idx:
                tmp[i] = q[i - 1] + q[i]
                i += 1
            q = tmp
            idx += 1
        return q