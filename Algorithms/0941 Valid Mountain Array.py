# Solution 1, simulation, two-pointer
# move pointer from both end and check it they meet in the middle
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        
        i = 0
        while i < n - 1 and A[i] < A[i + 1]:
            i += 1
        
        j = n - 1
        while j > i and A[j] < A[j - 1]:
            j -= 1
        
        return i == j and i != 0 and i != n - 1