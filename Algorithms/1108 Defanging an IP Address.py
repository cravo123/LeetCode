# Solution 1, manual replace
class Solution:
    def defangIPaddr(self, address: str) -> str:
        q = []
        
        for c in address:
            if c != '.':
                q.append(c)
            else:
                q.append('[.]')
        
        res = ''.join(q)
        
        return res

# Solution 2, use built-in
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = '[.]'.join(address.split('.'))
        
        return res

# Solution 2.1, another built-in
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')