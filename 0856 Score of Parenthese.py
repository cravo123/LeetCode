class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        q = []
        curr = 0
        for c in S:
            if c == '(':
                q.append(c)
            else:
                curr = 0
                while q and q[-1] != '(':
                    curr += q.pop()
                q.pop()
                curr = max(curr * 2, 1)
                q.append(curr)
        
        return sum(q)
    
# Solution 2,
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        q = []
        curr = 0
        for c in S:
            if c == '(':
                q.append(curr)
                curr = 0
            else:
                curr += q.pop() + max(curr, 1)
        
        return curr