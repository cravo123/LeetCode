class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)] # [[]] * numRows
        
        i, di = 0, 1
        
        for c in s:
            res[i].append(c)
            i += di
            if i == numRows:
                i = numRows - 2
                di = -1
            elif i == -1:
                i = 1
                di = 1
        res = ''.join(''.join(row) for row in res)
        
        return res