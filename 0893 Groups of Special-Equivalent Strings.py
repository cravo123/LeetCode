class Solution:
    def change(self, S):
        odd, even = [], []
        for i, c in enumerate(S):
            if i % 2 == 0:
                even.append(c)
            else:
                odd.append(c)
        odd.sort()
        even.sort()
        odd = ''.join(odd)
        even = ''.join(even)
        
        return odd, even
        
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        
        for a in A:
            res.add(self.change(a))
        
        return len(res)