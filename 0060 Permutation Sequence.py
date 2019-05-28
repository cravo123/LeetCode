# Solution 1, simulation
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        cans = [i for i in range(1, n + 1)]
        
        factorial = 1
        for i in range(1, n):
            factorial *= i
        # or factorial = math.factorial(n - 1)
        res = []
        
        while n > 0:
            n -= 1
            idx, k = divmod(k, factorial)
            factorial //= max(n, 1)
            res.append(cans[idx])
            cans.pop(idx)
            
        
        res = ''.join(str(c) for c in res)
        return res

# Solution 1.1, use seen list to mark if this digit is used or not
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        vs = [i for i in range(1, n + 1)]
        seen = [False for _ in vs]
        
        k -= 1
        res = []
        
        factorial = 1
        for i in range(1, n):
            factorial *= i
        
        while n > 0:
            n -= 1
            idx, k = divmod(k, factorial)
            factorial //= max(n, 1)
            
            # Find available digit to be appended to res
            j = 0
            while j < len(vs):
                if seen[j] == False:
                    if idx == 0:
                        res.append(vs[j])
                        seen[j] = True
                        break
                    idx -= 1
                j += 1
            
        res = ''.join(str(c) for c in res)
        return res