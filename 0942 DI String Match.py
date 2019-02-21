class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        n = len(S)
        i, j = 0, n
        
        res = [0 for _ in range(n + 1)]
        idx = 0
        while idx < n:
            if S[idx] == 'I':
                res[idx] = i
                i += 1
            else:
                res[idx] = j
                j -= 1
            idx += 1
        res[idx] = i
        return res
