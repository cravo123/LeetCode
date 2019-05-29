import collections

# Solution 1, use (ord(S[i]) - ord(S[0]) + 26) % 26 as encoding method
# There are other encoding method as well, say 
# (ord(S[i]) - ord(S[i - 1]) + 26) % 26 also works
class Solution(object):
    def change(self, word):
        if not word:
            return tuple()
        q = []
        base = ord(word[0])
        
        for c in word:
            q.append((ord(c) - base + 26) % 26)
        
        q = tuple(q)
        
        return q
    # or 1-line
    def normalize(self, s):
        q = [(ord(c) - ord(s[0]) + 26) % 26 for c in s]
        
        return tuple(q)
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        
        for word in strings:
            d[self.change(word)].append(word)
        
        res = list(d.values())
        
        return res