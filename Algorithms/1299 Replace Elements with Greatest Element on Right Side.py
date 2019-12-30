# Solution 1, simulation
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # right_max[i] is the maximum values from arr[(i + 1):]
        right_max = [-1 for _ in arr]
        
        n = len(arr)
        
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i + 1])
        
        return right_max
        