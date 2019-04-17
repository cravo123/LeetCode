import collections

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
                    