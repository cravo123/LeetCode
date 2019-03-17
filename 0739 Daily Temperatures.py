class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in T]
        
        q = []
        
        for i, c in enumerate(T):
            while q and T[q[-1]] < c:
                j = q.pop()
                res[j] = i - j
            q.append(i)
        
        return res