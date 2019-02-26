class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        
        n = len(s)
        
        for i in range(0, n, 2 * k):
            left, right = i, min(i + k - 1, n - 1) # Key to cap right index
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        res = ''.join(s)
        
        return res