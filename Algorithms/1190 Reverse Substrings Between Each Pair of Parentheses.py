# Solution 1, stack
# This problem tests recursion, so we can stack to solve it
class Solution:
    def reverseParentheses(self, s: str) -> str:
        q = []
        
        for c in s:
            if c != ')':
                q.append(c)
            else:
                tmp = []
                while q[-1] != '(':
                    tmp.append(q.pop())
                q.pop() # pop '('
                q.extend(tmp)
        res = ''.join(q)
        
        return res

# Solution 2, real recursion
# TO DO: solve it using recursion function