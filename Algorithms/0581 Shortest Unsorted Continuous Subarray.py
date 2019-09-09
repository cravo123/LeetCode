# Solution 1, sorting
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[::]
        tmp.sort()
        
        i, j = 0, len(nums) - 1
        
        while i <= j and nums[i] == tmp[i]:
            i += 1
        
        while i <= j and nums[j] == tmp[j]:
            j -= 1
        
        return j - i + 1

# Solution 1.1 sorting elegant
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[::]
        tmp.sort()
        
        left, right = len(nums), 0
        
        for i in range(len(nums)):
            if nums[i] != tmp[i]:
                left = min(left, i)
                right = max(right, i)
        
        return right - left + 1 if left <= right else 0