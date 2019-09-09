# Solution 1, two-pointer
class Solution:
    def reverse_help(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        
        i, flag = 0, True
        
        while i < n:
            if flag:
                self.reverse_help(s, i, min(i + k - 1, n - 1))
            i += k
            flag = not flag
        
        res = ''.join(s)
        
        return res