class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [None for _ in A]
        B = [[c, i] for i, c in enumerate(B)]
        B.sort()
        
        i = 0
        residuals = []
        for v in sorted(A):
            if v <= B[i][0]:
                residuals.append(v)
            else:
                res[B[i][1]] = v
                i += 1
        
        for i in range(len(A)):
            if res[i] is None:
                res[i] = residuals.pop()
        
        return res