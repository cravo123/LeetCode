import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, need row, col and count as indexing
# This is because at last we sort by row number
class Solution:
    def dfs(self, node, row, col, res):
        if node is None:
            return
        self.dfs(node.left, row + 1, col - 1, res)
        res[col].append([row, self.idx, node.val])
        self.idx += 1
        self.dfs(node.right, row + 1, col + 1, res)
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = collections.defaultdict(list)
        self.idx = 0
        self.dfs(root, 0, 0, res)
        
        sorted_res = []
        
        for col in sorted(res):
            res[col].sort()
            sorted_res.append([x for _, _, x in res[col]])
        
        return sorted_res

# Solution 2, BFS level-order traversing is easier
# since in BFS, we don't need to sort by rows
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        if root is None:
            return []
        
        q = [[root, 0]]
        
        while q:
            tmp = []
            for p, col in q:
                d[col].append(p.val)
                if p.left:
                    tmp.append([p.left, col - 1])
                if p.right:
                    tmp.append([p.right, col + 1])
            q = tmp
        
        res = [d[col] for col in sorted(d)]
        
        return res