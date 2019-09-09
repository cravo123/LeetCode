# Solution 1, two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left = right = 0
        res = 0
        
        while i <= j:
            if height[i] <= height[j]:
                res += max(0, left - height[i])
                left = max(left, height[i])
                i += 1
            else:
                res += max(0, right - height[j])
                right = max(right, height[j])
                j -= 1
        return res

# Solution 2, Stack

# Solution 3,

