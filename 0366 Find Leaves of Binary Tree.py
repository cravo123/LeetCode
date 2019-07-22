import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, cache node depth, and generate output
class Solution:
    def dfs(self, node, d):
        if node is None:
            return 0
        L, R = self.dfs(node.left, d), self.dfs(node.right, d)
        h = max(L, R) + 1
        d[h].append(node.val)
        
        return h
        
        
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        self.dfs(root, d)
        
        res = [d[x] for x in sorted(d)]
        
        return res

# Solution 2, update node children each time
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        if root is None:
            return res
        
        while root.left or root.right:
            path = []
            q = [root]
            
            while q:
                p = q.pop()
                # extract leaves
                if p.left and p.left.left is None and p.left.right is None:
                    path.append(p.left.val)
                    p.left = None
                if p.right and p.right.left is None and p.right.right is None:
                    path.append(p.right.val)
                    p.right = None
                
                if p.right:
                    q.append(p.right)
                if p.left:
                    q.append(p.left)
            res.append(path)
        res.append([root.val])
        
        return res

# Solution 2.1, recursion version
class Solution:
    def dfs(self, node, q):
        if node is None:
            return
        if node.left is None and node.right is None:
            q.append(node.val)
            return
        node.left = self.dfs(node.left, q)
        node.right = self.dfs(node.right, q)
        
        return node
        
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        curr = root
        
        while curr:
            q = []
            curr = self.dfs(curr, q)
            res.append(q)
        
        return res