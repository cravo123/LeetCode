# Solution 1, greedy
# After sorting, then three edges a < b < c constitute a triangle
# as long as a + b > c
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        
        i, n = 0, len(A)
        
        while i < len(A) - 2:
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
            i += 1
        
        return 0