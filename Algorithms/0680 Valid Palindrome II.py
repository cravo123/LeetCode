class Solution:
    def is_palindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        
        return left >= right
    
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        if i >= j:
            return True
        
        return self.is_palindrome(s, i, j - 1) or self.is_palindrome(s, i + 1, j)