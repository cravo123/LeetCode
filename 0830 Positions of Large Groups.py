class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        if not S:
            return res
        
        curr = S[0]
        cnt = 0
        for i, c in enumerate(S):
            if c == curr:
                cnt += 1
            else:
                if cnt >= 3:
                    res.append([i - cnt , i - 1])
                cnt = 1
                curr = c
        
        if cnt >= 3:
            res.append([len(S) - cnt , len(S) - 1])
        
        return res

# Solution 2, more precise control of iterator
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        if not S:
            return res
        
        i, n = 0, len(S)
        
        while i < n:
            j = i
            cnt = 0
            while j < n and S[i] == S[j]:
                cnt += 1
                j += 1
            
            if cnt >= 3:
                res.append([i, j - 1])
            i = j
        
        return res