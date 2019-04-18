# Solution 1, Iteration
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        sign = -1 if num < 0 else 1
        
        num = abs(num)
        
        q = []
        
        while num > 0:
            num, v = divmod(num, 7)
            q.append(v)
        
        res = ''.join(str(x) for x in reversed(q))
        
        return res if sign == 1 else '-' + res

# Solution 2, Recursion
class Solution(object):
    def dfs(self, num):
        if num < 0:
            return '-' + self.dfs(abs(num))
        
        if num < 7:
            return str(num)
        
        return self.dfs(num // 7) + str(num % 7)
        
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        return self.dfs(num)