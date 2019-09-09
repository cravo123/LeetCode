# Solution 1, simulation
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        # find minimum
        res = A[0]
        for c in A:
            if c < res:
                res = c
        
        res = sum(map(int, str(res)))
        
        return 1 - res % 2

# Solution 2, built-in
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        res = sum(map(int, str(min(A))))
        
        return 1 - res % 2 