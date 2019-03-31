class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        
        curr = 0
        for c in A:
            curr = curr * 2 + c
            if curr % 5 == 0:
                flag = True
            else:
                flag = False
            res.append(flag)
        
        return res