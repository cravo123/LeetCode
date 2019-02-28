import collections
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = collections.Counter(s)
        
        if d['A'] > 1 or 'LLL' in s:
            return False
        return True