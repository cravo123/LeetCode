# Solution 1, greedy
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        
        curr = 0
        i = 0
        while i < len(arr):
            curr += arr[i]
            
            if curr > 5000:
                break
            
            i += 1
        
        return i
        