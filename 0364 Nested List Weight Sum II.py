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

# Solution 1, two-pass
# First pass to get depth, and second path to sum up
class Solution:
    def depth(self, nestedList):
        if not nestedList:
            return 0
        if nestedList.isInteger():
            return 1
        curr = 0
        for p in nestedList.getList():
            curr = max(curr, self.depth(p) + 1)
        
        return curr
        
    def dfs(self, nestedList, level):
        if not nestedList:
            return
        
        if nestedList.isInteger():
            self.res += nestedList.getInteger() * level
            return
        
        for x in nestedList.getList():
            self.dfs(x, level - 1)
        
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        
        self.res = 0
        self.h = max(self.depth(p) for p in nestedList)
        
        for p in nestedList:
            self.dfs(p, self.h)
        
        return self.res

# Solution 2, One-pass elegant 
# Maintain a level sum, and add to final result
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        curr = 0
        
        q = nestedList
        
        while q:
            tmp = []
        
            for p in q:
                if p.isInteger():
                    curr += p.getInteger()
                else:
                    tmp.extend(p.getList())
            res += curr
            q = tmp
        return res        