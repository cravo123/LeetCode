# Solution 1, two-pass
# cache pre-index and post-index whose values are C
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

# Solution 1.1, one-pass
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        q = [float('-inf')]
        
        for i, c in enumerate(S):
            if c == C:
                q.append(i)
        
        q.append(float('inf'))
        
        res = []
        curr = 0
        
        for i in range(len(S)):
            while q[curr] <= i:
                curr += 1
            res.append(min(q[curr] - i, i - q[curr - 1]))
        
        return res
        