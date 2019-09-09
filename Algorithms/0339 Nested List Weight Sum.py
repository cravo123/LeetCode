# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Solution 1, using Stack, need to cache current depth
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        
        q = [[x, 1] for x in nestedList]
        
        while q:
            p, curr_depth = q.pop()
            if p.isInteger():
                res += curr_depth * p.getInteger()
            else:
                curr_depth += 1
                for c in p.getList():
                    q.append([c, curr_depth])
        
        return res

# Solution 2, DFS
class Solution:
    def dfs(self, node, level):
        if node.isInteger():
            return node.getInteger() * level
        
        res = 0
        level += 1
        for p in node.getList():
            res += self.dfs(p, level)
        
        return res
        
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        res = 0
        for p in nestedList:
            res += self.dfs(p, 1)
        
        return res

# Solution 3, BFS, level-traversal
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        level = 1
        q = nestedList
        
        while q:
            tmp = []
            for p in q:
                if p.isInteger():
                    res += level * p.getInteger()
                else:
                    tmp.extend(p.getList())
            level += 1
            q = tmp
        return res