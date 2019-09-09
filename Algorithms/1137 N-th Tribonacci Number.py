# Solution 1, O(1) memory DP
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b, c = 0, 1, 1
        idx = 2
        while idx < n:
            a, b, c = b, c, a + b + c
            idx += 1
        
        return c

# Solution 2, O(n) DP
class Solution:
    def tribonacci(self, n: int) -> int:
        q = [0 for _ in range(max(n + 1, 3))]
        q[1] = q[2] = 1
        
        for i in range(3, n + 1):
            q[i] = q[i - 1] + q[i - 2] + q[i - 3]
        
        return q[n]