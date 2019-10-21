# Solution 1, check sum, O(n)
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)

# Solution 2, simulation, O(n)
# First find out the increment, then check each element
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        
        for i in range(1, n):
            if arr[i] != arr[i - 1] + diff:
                return arr[i - 1] + diff

# Solution 3, binary search
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        
        i, j = 0, n - 1
        
        while i < j:
            m = (i + j) // 2
            curr = arr[m]
            need = arr[0] + m * diff
            
            if need == curr:
                i = m + 1
            else:
                j = m
        
        return arr[0] + i * diff