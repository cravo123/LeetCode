# Solution 1, factorization, greedy
# Since we only each digit should between 2 to 9 (1 is useless, and make our result larger)
# we can then try adding each digit to result in reversing order
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 10:
            return a
        
        q = []
        
        for v in range(9, 1, -1):
            while a > 0 and a % v == 0:
                q.append(v)
                a //= v
        
        if a > 1:
            return 0
        
        q.sort()
        
        res = int(''.join(str(c) for c in q))
        
        return res if res < 2 ** 31 else 0


# Solution 2, complex back-tracking.
class Solution:
    def dfs(self, v, d):
        if v < 10:
            return [v]
        if v in d:
            return d[v]
        
        x = int(v ** 0.5)
        res = []
        while x > 1:
            if v % x == 0:
                left, right = self.dfs(x, d), self.dfs(v // x, d)
                if left and right:
                    q = left + right
                    q.sort()
                    if res == [] or len(q) < len(res) or (len(q) == len(res) and any(a < b for a, b in zip(q, res))):
                        res = q
            x -= 1
        d[v] = res
        return res
        
        
    def smallestFactorization(self, a: int) -> int:
        d = {}
        q = self.dfs(a, d)
        if not q:
            return 0
        q.reverse()
        res = int(''.join(str(c) for c in q))
        return res if res < 2 ** 31 else 0