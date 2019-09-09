import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, memorization
# Observation: left and right subtree nodes count can only be odd
class Solution:
    def dfs(self, N, d):
        if N in d:
            return d[N]
        
        if N == 1:
            d[N].append(TreeNode(0))
            return d[N]
        
        for i in range(1, N - 1, 2):
            L, R = i, N - 1 - i
            if (L - R) % 2 == 0:
                for left_node in self.dfs(L, d):
                    for right_node in self.dfs(R, d):
                        root = TreeNode(0)
                        root.left = left_node
                        root.right = right_node
                        d[N].append(root)
        
        return d[N]
        
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        d = collections.defaultdict(list)
        d[0].append(None)
        
        self.dfs(N, d)
        
        return d[N]

# Solution 1.1, a better implementation
class Solution:
    def dfs(self, n, d):
        if n in d:
            return d[n]
        if n == 0:
            res = [None]
        elif n == 1:
            res = [TreeNode(0)]
        elif n < 0 or n % 2 == 0:
            res = []
        else:
            res = []
            
            for l_cnt in range(1, n, 2):
                for l_t in self.dfs(l_cnt, d):
                    for r_t in self.dfs(n - 1 - l_cnt, d):
                        t = TreeNode(0)
                        t.left = l_t
                        t.right = r_t
                        res.append(t)
        d[n] = res
        
        return res
        
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        d = collections.defaultdict(list)
        
        self.dfs(N, d)
        
        return d[N]