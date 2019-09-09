import collections

# Same as LC 0758
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        d = collections.defaultdict(set)
        
        for word in dict:
            d[len(word)].add(word)
        
        
        i, n = 0, len(s)
        
        flag = [False for _ in s]
        
        while i < n:
            for c in sorted(d, reverse=True):
                if i + c <= n and s[i:(i + c)] in d[c]:
                    flag[i:(i + c)] = [True for _ in range(i, i + c)]
            
            i += 1
        
        res = []
        i = 0
        while i < n:
            if flag[i]:
                j = i
                while j < n and flag[j]:
                    j += 1
                res.append('<b>%s</b>' % s[i:j])
                i = j
            else:
                res.append(s[i])
                i += 1
        res = ''.join(res)
        
        return res