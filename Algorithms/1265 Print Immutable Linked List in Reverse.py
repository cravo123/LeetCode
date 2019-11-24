# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

# Solution 1, simulation
# Save all nodes in stack and print reversely
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        q = []
        
        curr = head
        while curr:
            q.append(curr)
            curr = curr.getNext()
        
        while q:
            q.pop().printValue()

# Solution 2, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 
        self.dfs(node.getNext())
        node.printValue()
        
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        self.dfs(head)