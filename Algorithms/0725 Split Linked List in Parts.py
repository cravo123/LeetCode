# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
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
        need = k
        for _ in range(k):
            if cnt == 0:
                res.append(None)
            else:
                need = (cnt - 1) // need + 1
                need -= 1
                cnt -= need
                res.append(curr)
                curr = self.extract(curr, need)
        
        return res

# Solution 1.1, another way to calculate split part length
# class Solution:
    def split(self, node, cnt):
        runner = node
        while runner and cnt > 1:
            runner = runner.next
            cnt -= 1
        
        if runner is None:
            return runner
        res = runner.next
        runner.next = None
        
        return res
        
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root is None:
            return [[] for _ in range(k)]
        
        cnt = 0
        curr = root
        while curr:
            cnt += 1
            curr = curr.next
        
        more = (cnt - 1) // k + 1
        more_cnt = cnt % k
        less = cnt // k
        less_cnt = k - more_cnt
        lens = [more] * more_cnt + [less] * less_cnt
        
        res = []
        curr = root
        
        for l in lens:
            tmp = self.split(curr, l)
            res.append(curr)
            curr = tmp
        
        return res
                      