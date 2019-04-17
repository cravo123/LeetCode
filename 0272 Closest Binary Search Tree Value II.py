# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

# Solution 1, deque
class Solution:
    def dfs(self, node, target, k, q):
        if node is None:
            return
        self.dfs(node.left, target, k, q)
        
        if len(q) == k:
            left = q.popleft()
            if abs(left - target) < abs(node.val - target):
                q.appendleft(left)
                return
            else:
                q.append(node.val)
        else:
            q.append(node.val)
        
        self.dfs(node.right, target, k, q)
        
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        q = collections.deque()
        
        self.dfs(root, target, k, q)
        
        res = list(q)
        
        return res

# Solution 2, use two stacks to traverse BST