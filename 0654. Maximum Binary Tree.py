# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, nums, left, right):
        if left > right:
            return
        
        max_val = max(nums[left:(right + 1)])
        max_idx = nums[left:(right + 1)].index(max_val) + left
        
        root = TreeNode(max_val)
        root.left = self.dfs(nums, left, max_idx - 1)
        root.right = self.dfs(nums, max_idx + 1, right)
        
        return root
        
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return
        
        res = self.dfs(nums, 0 , len(nums) - 1)
        return res

# Iteration
class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        q = []
        
        for c in nums:
            new_node = TreeNode(c)
            while q and q[-1].val < c:
                new_node.left = q.pop()
            if q:
                q[-1].right = new_node
            q.append(new_node)
        
        return q[0]
        
