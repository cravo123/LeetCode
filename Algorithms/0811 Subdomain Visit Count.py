import collections

# Solution 1, simulation, hashmap
class Solution:
    def add(self, address, d):
        num, name = address.split()
        num = int(num)
        name = name.split('.')
        
        for i in range(len(name)):
            d[tuple(name[i:])] += num
        
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = collections.Counter()
        
        for address in cpdomains:
            self.add(address, d)
        
        res = ['%d %s' % (cnt, '.'.join(name)) for name, cnt in d.items()]
        
        return res