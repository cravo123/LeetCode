import collections
# Say you have n same cards, you divive to k groups where 
# each group has the same number. Then it means the count of each 
# group must be a divisor of n. That is the reason why we use gcd
# greatest common divisor here.
class Solution:
    def gcd(self, a, b):
        if a == 0 or b == 0:
            return 0
        while b != 0:
            a, b = b, a % b
        return a
    
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = collections.Counter(deck)
        
        res = None
        
        for c in d.values():
            if res is None:
                res = c
            else:
                res = self.gcd(res, c)
        return res >= 2