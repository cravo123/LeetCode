# Solution 1, Use string length as delimitors
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + ' ' + s)
        
        res = ''.join(res)
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s:
            return res
        i, n = 0, len(s)
        
        while i < n:
            cnt = 0
            while i < n and s[i].isdigit():
                cnt = cnt * 10 + int(s[i])
                i += 1
            i += 1 # skip space
            res.append(s[i:(i + cnt)])
            i += cnt
        return res

# Solution 2, Real escaping
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        
        for s in strs:
            s = s.replace('#', '##')
            res.append(s)
        res.append('') # distinguish between [] and ['']
        res = ' # '.join(res)
        
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        s = s.split(' # ')
        res = []
        for x in s:
            x = x.replace('##', '#')
            res.append(x)
        return res[:-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))