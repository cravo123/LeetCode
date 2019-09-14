# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def dfs(self, start, end, nums):
        if start > end:
            return 
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(start, mid - 1, nums)
        root.right = self.dfs(mid + 1, end, nums)
        
        return root
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        res = self.dfs(0, len(nums) - 1, nums)
        
        return res