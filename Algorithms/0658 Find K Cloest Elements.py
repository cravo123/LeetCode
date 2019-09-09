class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        
        while right - left + 1 > k:
            L, R = abs(arr[left] - x), abs(arr[right] - x)
            
            if L <= R:
                right -= 1
            else:
                left += 1
        return arr[left:(right + 1)]