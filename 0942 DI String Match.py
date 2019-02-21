# Solution 1,
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

# Solution 2,
class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        left = right = 0
        res = [0]

        for c in S:
            if c == 'I':
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        res = [x - left for x in res]
        return res
