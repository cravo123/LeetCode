# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, reverse -> merge -> reverse back
class Solution:
    def reverse(self, node):
        prev, curr = None, node
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p    
        return prev
    
    def merge(self, p, q):
        dummy = curr = ListNode(0)
        
        carry = 0
        while p or q or carry:
            if p:
                carry += p.val
                p = p.next
            if q:
                carry += q.val
                q = q.next
            carry, v = divmod(carry, 10)
            curr.next = ListNode(v)
            curr = curr.next
        
        return dummy.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reverse(l1), self.reverse(l2)
        
        res = self.merge(l1, l2)
        
        res = self.reverse(res)
        
        return res

# Solution 2, using stack
class Solution:
    def collect_vals(self, node):
        q = []
        
        while node:
            q.append(node.val)
            node = node.next
        
        return q
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1, q2 = map(self.collect_vals, (l1, l2))
        
        curr = ListNode(0)
        carry = 0
        
        while q1 or q2 or carry:
            if q1:
                carry += q1.pop()
            if q2:
                carry += q2.pop()
            
            carry, val = divmod(carry, 10)
            tmp = ListNode(val)
            tmp.next = curr.next
            curr.next = tmp
        
        return curr.next