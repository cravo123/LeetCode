# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

# Solution 1, record leaf node
# Actually no need to record leaf node, if a node only has one neighbor,
# which is its parent, then it is a leaf node.
class Solution:
    def dfs(self, node, d, leaves):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            leaves.add(node.val)
            return
        
        if node.left:
            d[node.val].add(node.left.val)
            d[node.left.val].add(node.val)
            self.dfs(node.left, d, leaves)
        
        if node.right:
            d[node.val].add(node.right.val)
            d[node.right.val].add(node.val)
            self.dfs(node.right, d, leaves)
        
        
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # build graph
        d = collections.defaultdict(set)
        leaves = set()
        self.dfs(root, d, leaves)
        
        seen = set()
        q = [k]
        seen.add(k)
        
        while q:
            tmp = []
            
            for v in q:
                if v in leaves:
                    return v
                for x in d[v]:
                    if x not in seen:
                        tmp.append(x)
                        seen.add(x)
            q = tmp
        
        return 

# Solution 2, no need to record leaf node
class Solution:
    def dfs(self, node, d):
        if node is None:
            return
        
        if node.left:
            d[node.val].add(node.left.val)
            d[node.left.val].add(node.val)
            self.dfs(node.left, d)
        if node.right:
            d[node.val].add(node.right.val)
            d[node.right.val].add(node.val)
            self.dfs(node.right, d)
        
        
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        d = collections.defaultdict(set)
        
        self.dfs(root, d)

        # This is necessary, if tree is [1, 2] with k = 1, 
        # then if we don't add None, it will return 1, which is wrong        
        if root:
            d[root.val].add(None)
        
        
        q = [k]
        seen = set()
        seen.add(k)
        while q:
            tmp = []
            
            for p in q:
                if len(d[p]) <= 1:
                    return p
                for x in d[p]:
                    if x is not None and x not in seen:
                        seen.add(x)
                        tmp.append(x)
            q = tmp