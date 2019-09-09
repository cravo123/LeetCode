import collections

# Solution 1, hash map
# Same as LC 0616
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        d = collections.defaultdict(set)
        
        for word in words:
            d[len(word)].add(word)
        
        
        i, n = 0, len(S)
        
        flag = [False for _ in S]
        
        while i < n:
            for c in sorted(d, reverse=True):
                if i + c <= n and S[i:(i + c)] in d[c]:
                    flag[i:(i + c)] = [True for _ in range(i, i + c)]
            
            i += 1
        
        res = []
        i = 0
        while i < n:
            if flag[i]:
                j = i
                while j < n and flag[j]:
                    j += 1
                res.append('<b>%s</b>' % S[i:j])
                i = j
            else:
                res.append(S[i])
                i += 1
        res = ''.join(res)
        
        return res

# Solution 1.1, similar idea
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        # precache length
        words = set(words)
        d = collections.defaultdict(set)
        for word in words:
            d[len(word)].add(word)
        
        # determine idx which will be bolded
        need = set()
        
        n = len(S)
        
        for i in range(n):
            for l in d:
                if S[i:(i + l)] in d[l]:
                    for k in range(i, i + l):
                        need.add(k)
        
        res = []
        i = 0
        
        while i < n:
            j = i
            while j < n and j not in need:
                j += 1
            res.append(S[i:j])
            
            i = j
            while j < n and j in need:
                j += 1
            
            if i < n:
                res.append('<b>')
                res.append(S[i:j])
                res.append('</b>')
            
            i = j
        
        res = ''.join(res)
        
        return res