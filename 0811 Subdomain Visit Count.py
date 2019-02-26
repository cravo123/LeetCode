import collections

class Solution:
    def add(self, name, d):
        cnt, name = name.split()
        
        name = name.split('.')
        cnt = int(cnt)
        
        n = len(name)
        for i in range(n):
            d[tuple(name[i:])] += cnt
        
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = collections.Counter()
        
        for name in cpdomains:
            self.add(name, d)
        
        res = ['%d %s' % (cnt, '.'.join(key)) for key, cnt in d.items()]
        
        return res