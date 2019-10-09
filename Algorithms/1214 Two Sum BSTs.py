# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion, O(m d) 
# d = log n if BST is balanced
class Solution:
    def dfs(self, node, target):
        if node is None:
            return False
        if node.val == target:
            return True
        if node.val < target:
            return self.dfs(node.right, target)
        return self.dfs(node.left, target)
    
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if root1 is None or root2 is None:
            return False
        
        return (self.dfs(root2, target - root1.val)
                or self.twoSumBSTs(root1.left, root2, target)
                or self.twoSumBSTs(root1.right, root2, target))

# Solution 2, iteration, two-pointer idea
class Solution:
    def push_left(self, node, q):
        curr = node
        while curr:
            q.append(curr)
            curr = curr.left
    
    def push_right(self, node, q):
        curr = node
        while curr:
            q.append(curr)
            curr = curr.right
    
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        q1, q2 = [], []
        
        self.push_left(root1, q1)
        self.push_right(root2, q2)
        
        while q1 and q2:
            n1 = q1[-1]
            n2 = q2[-1]
            
            curr_val = n1.val + n2.val
            
            if curr_val == target:
                return True
            
            if curr_val < target:
                curr = q1.pop()
                curr = curr.right
                self.push_left(curr, q1)
            else:
                curr = q2.pop()
                curr = curr.left
                self.push_right(curr, q2)
        return False