"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def dfs(self, p, q):
        if p.isLeaf:
            if p.val:
                return p
            return q
        if q.isLeaf:
            if q.val:
                return q
            return p
        
        TL = self.dfs(p.topLeft, q.topLeft)
        TR = self.dfs(p.topRight, q.topRight)
        BL = self.dfs(p.bottomLeft, q.bottomLeft)
        BR = self.dfs(p.bottomRight, q.bottomRight)
        
        if TL.isLeaf and TR.isLeaf and BL.isLeaf and BR.isLeaf:
            if TL.val == TR.val == BL.val == BR.val:
                return Node(TL.val, True, None, None, None, None)
        
        res = Node(False, False, TL, TR, BL, BR)
        
        return res
        
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        return self.dfs(quadTree1, quadTree2)