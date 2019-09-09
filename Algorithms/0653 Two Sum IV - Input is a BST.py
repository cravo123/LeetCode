# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, in-order traverse BST to change it to a sorted list
# then 2-pointer 
class Solution:
    def dfs(self, node, q):
        if node is None:
            return
        self.dfs(node.left, q)
        q.append(node.val)
        self.dfs(node.right, q)
        
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        q = []
        
        self.dfs(root, q)
        
        i, j = 0, len(q) - 1
        
        while i < j:
            v = q[i] + q[j]
            if v < k:
                i += 1
            elif v > k:
                j -= 1
            else:
                return True
        return False

# Solution 1.1, recursion hashset
class Solution:
    def dfs(self, node, target, d):
        if node is None:
            return False
        if target - node.val in d:
            return True
        d.add(node.val)
        
        return self.dfs(node.left, target, d) or self.dfs(node.right, target, d)
        
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        d = set()
        
        return self.dfs(root, k, d)

# Solution 1.2, iteration hashset
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                
                if k - p.val in d:
                    return True
                d.add(p.val)
                
                p = p.right
        
        return False

# Solution 2, Recursion, Search each pairs
class Solution:
    def dfs(self, node, target):
        if node is None:
            return False
        if node.val < target:
            return self.dfs(node.right, target)
        if node.val > target:
            return self.dfs(node.left, target)
        return True
    
    def check_sum(self, node, root, k):
        if node is None:
            return False
        if node.val * 2 != k and self.dfs(root, k - node.val):
            return True
        
        return self.check_sum(node.left, root, k) or self.check_sum(node.right, root, k)
        
        
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        if root is None:
            return False
        
        return self.check_sum(root, root, k)