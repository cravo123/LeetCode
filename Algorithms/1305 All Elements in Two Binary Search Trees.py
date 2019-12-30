# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, iteration on two trees simultaneously
class Solution:
    def push_stack(self, node, path):
        while node:
            path.append(node)
            node = node.left
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1, s2 = [], []
        
        self.push_stack(root1, s1)
        self.push_stack(root2, s2)
        
        res = []
        
        while s1 and s2:
            v1 = s1[-1].val
            v2 = s2[-1].val
            
            res.append(min(v1, v2))
            
            if v1 <= v2:
                node = s1.pop()
                node = node.right
                self.push_stack(node, s1)
            else:
                node = s2.pop()
                node = node.right
                self.push_stack(node, s2)
        
        for s in [s1, s2]:
            while s:
                node = s.pop()
                res.append(node.val)
                
                node = node.right
                self.push_stack(node, s)
        
        return res

# Solution 2, recursion with merge sort idea
class Solution:
    def dfs(self, node, path):
        if node is None:
            return
        
        self.dfs(node.left, path)
        path.append(node.val)
        self.dfs(node.right, path)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        path1 = []
        path2 = []
        
        # Cache all vals
        self.dfs(root1, path1)
        self.dfs(root2, path2)
        
        # Here we can use merge-sort idea to make it O(n)
        # res = self.merge(path1, path2)
        res = path1 + path2
        res =list(sorted(res))
        
        return res
    
    def merge(self, l1, l2):
        """Only used for merge-sort idea"""
        res = []
        n1, n2 = len(l1), len(l2)
        i1 = i2 = 0
        
        while i1 < n1 and i2 < n2:
            val = min(l1[i1], l2[i2])
            
            if val == l1[i1]:
                i1 += 1
            else:
                i2 += 1
            
            res.append(val)
        
        while i1 < n1:
            res.append(l1[i1])
            i1 += 1
        
        while i2 < n2:
            res.append(l2[i2])
            i2 += 1
        
        return res