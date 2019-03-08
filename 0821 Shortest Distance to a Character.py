class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        res = [float('inf') for _ in S]
        
        last = float('-inf')
        for i in range(len(S)):
            if S[i] == C:
                last = i
            res[i] = min(res[i], i - last)
        
        last = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                last = i
            res[i] = min(res[i], last - i)
        
        return res
        