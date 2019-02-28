# Solution 1
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        q = []
        
        while n > 0:
            q.append((n - 1) % 26)
            n = (n - 1) // 26
            
        res = [chr(ord('A') + c) for c in q]
        res = ''.join(reversed(res))
        
        return res

# Solution 2
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        q = []
        
        while n > 0:
            n -= 1
            q.append(n % 26)
            n //= 26
            
        res = [chr(ord('A') + c) for c in q]
        res = ''.join(reversed(res))
        
        return res

# Note Excel column is different from x-nary number
# in n-ary, it is illegal to write '00'
# but in Excel column, it is ok to write 'AA'