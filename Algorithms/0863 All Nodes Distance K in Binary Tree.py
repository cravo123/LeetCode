import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, hashmap to store all connections
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

    def bfs(self, start, steps, d):
        seen = set()
        q = [start]
        seen.add(start)
        curr = 0
        while curr < steps:
            tmp = []
            for p in q:
                for x in d[p]:
                    if x not in seen:
                        seen.add(x)
                        tmp.append(x)
            curr += 1
            q = tmp
            
        return q
            
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        d = collections.defaultdict(set)
        
        self.dfs(root, d)
        
        res = self.bfs(target.val, K, d)
        
        return res

# Solution 2, Add parent to each node
class Solution:
    def add_parent(self, node, parent):
        if node is None:
            return
        node.parent = parent
        
        self.add_parent(node.left, node)
        self.add_parent(node.right, node)
    
    def bfs(self, node, steps):
        q = [node]
        seen = set()
        seen.add(node.val)
        curr = 0
        
        while curr < steps:
            tmp = []
            
            for p in q:
                for x in [p.parent, p.left, p.right]:
                    if x and x.val not in seen:
                        tmp.append(x)
                        seen.add(x.val)
            curr += 1
            q = tmp
        res = [p.val for p in q]
        
        return res
    
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        self.add_parent(root, None)
        
        res = self.bfs(target, K)
        
        return res