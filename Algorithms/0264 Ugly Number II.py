from heapq import heappop, heappush

# Solution 1, three pointers
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1 for _ in range(n)]
        
        t2 = t3 = t5 = 0
        i = 1
        while i < n:
            res[i] = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            
            if res[t2] * 2 == res[i]:
                t2 += 1
            
            if res[t3] * 3 == res[i]:
                t3 += 1
            
            if res[t5] * 5 == res[i]:
                t5 += 1
            
            i += 1
        
        return res[n - 1]

# Solution 2, heap solution, TLE
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = set()
        
        q = [1]
        
        while len(res) < n:
            v = heappop(q)
            res.add(v)
            heappush(q, 2 * v)
            heappush(q, 3 * v)
            heappush(q, 5 * v)
        
        return v

# Solution 3, DP, TLE
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        d = set([1])
        
        cnt = 1
        v = 2
        while cnt < n:
            for c in [2, 3, 5]:
                if v % c == 0 and v // c in d:
                    d.add(v)
                    cnt += 1
                    break
            v += 1
        return v - 1
