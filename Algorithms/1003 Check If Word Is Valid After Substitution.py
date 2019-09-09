# Solution 1, brute-force, O(n ^ 2)
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        while 'abc' in S:
            idx = S.find('abc')
            S = S[:idx] + S[(idx + 3):]
        
        return S == ''

# Solution 2, same brute-force, but use stack, O(n)
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        q = []
        
        for c in S:
            q.append(c)
            
            while len(q) >= 3 and q[-3:] == ['a', 'b', 'c']:
                q.pop()
                q.pop()
                q.pop()
        
        return len(q) == 0

# Solution 3, same idea as Solution 2, but with pruning(early-termination)
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        q = []
        
        for c in S:
            q.append(c)
            
            if c == 'c':
                if len(q) < 3 or q[-3:] != ['a', 'b', 'c']:
                    return False
                q.pop()
                q.pop()
                q.pop()
        
        return len(q) == 0