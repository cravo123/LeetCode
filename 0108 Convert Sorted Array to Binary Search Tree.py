# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, nums, start, end):
        if start > end:
            return 
        if start == end:
            return TreeNode(nums[start])
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, end)
        
        return root
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        res = self.dfs(nums, 0, len(nums) - 1)
        
        return res