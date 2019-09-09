# Solution 1, simulation
# if 23457 in N, return False
# then check if after rotation, value doesn't change
class Solution:
    def confusingNumber(self, N: int) -> bool:
        N = str(N)
        
        if len(set(list('23457')) & set(N)) > 0:
            return False
        
        d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        
        i, n = 0, len(N)
        
        while i <= n // 2:
            if N[n - i - 1] == d[N[i]]:
                i += 1
            else:
                return True
        return False

# Solution 1.1, better implementation
class Solution:
    def confusingNumber(self, N: int) -> bool:
        d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        
        q = []
        
        S = str(N)
        
        for c in reversed(S):
            if c not in d:
                return False
            q.append(d[c])
        
        return False if ''.join(q) == S else True