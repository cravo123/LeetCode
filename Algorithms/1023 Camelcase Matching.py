# Solution 1, simulation
class Solution:
    def match(self, query, pattern):
        m, n = map(len, (query, pattern))
        i = j = 0
        
        while i < m and j < n:
            if query[i].isupper() and query[i] != pattern[j]:
                return False
            if query[i] == pattern[j]:
                j += 1
            i += 1
        
        if j < n:
            return False
        
        while i < m:
            if query[i].isupper():
                return False
            i += 1
        return True     
        
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        res = [self.match(query, pattern) for query in queries]
        
        return res

# Solution 1.1, similar idea
class Solution:
    def match(self, query, pattern):
        if len(query) < len(pattern):
            return False
        j, m = 0, len(pattern)
        
        for c in query:
            if c.upper() == c:
                if j == m or pattern[j] != c:
                    return False
                j += 1
            elif j < m and c == pattern[j]:
                j += 1
        
        return True if j == m else False
        
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [self.match(query, pattern) for query in queries]
        
        return res