import collections

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, stack solution
class Solution:
    def get_length(self, node):
        res = 0
        while node:
            res += 1
            node = node.next
        return res
        
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        n = self.get_length(head)
        
        res = [0 for _ in range(n)]
        
        q = []
        curr = head
        i = 0
        while curr:
            while q and q[-1][1] < curr.val:
                j, _ = q.pop()
                res[j] = curr.val
            q.append([i, curr.val])
            i += 1
            curr = curr.next
        
        return res

# Solution 1.1, a more elegant solution
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        cnt = 0
        q = []
        
        curr = head
        d = collections.Counter()
        
        while curr:
            while q and q[-1][1] < curr.val:
                i, val = q.pop()
                d[i] = curr.val
            q.append([cnt, curr.val])
            curr = curr.next
            cnt += 1
        
        res = [d[i] for i in range(cnt)]
        
        return res