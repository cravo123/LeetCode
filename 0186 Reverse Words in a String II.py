class Solution:
    def reverse(self, A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        
    def reverseWords(self, A: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        n = len(A)
        self.reverse(A, 0, n - 1)
        
        i = 0
        while i < n:
            j = i
            while j < n and A[j] != ' ':
                j += 1
            self.reverse(A, i, j - 1)
            i = j + 1