# Solution 1, greedy
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        res = [0 for _ in range(n + 1)]
        
        left, right = 0, n
        
        for i in range(n):
            if S[i] == 'I':
                res[i] = left
                left += 1
            else:
                res[i] = right
                right -= 1
        res[n] = left
        
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
