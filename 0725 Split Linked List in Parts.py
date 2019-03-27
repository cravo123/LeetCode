# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, node):
        res = 0
        while node:
            res += 1
            node = node.next
        return res
    
    def extract(self, node, need):
        curr = node
        idx = 0
        while idx < need - 1:
            curr = curr.next
            idx += 1
        
        res = curr.next
        curr.next = None
        
        return res
    
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cnt = self.length(root)
        
        res = []
        curr = root
        
        for _ in range(k):
            if cnt == 0:
                res.append(None)
            else:
                need = (cnt - 1) // k + 1
                k -= 1
                cnt -= need
                res.append(curr)
                curr = self.extract(curr, need)
        
        return res
                
                
            