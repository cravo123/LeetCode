import itertools

# Solution 1, manual check
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        v1 = list(map(int, v1))
        v2 = list(map(int, v2))
        
        m, n = len(v1), len(v2)
        
        for i in range(min(m, n)):    
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1
        
        i = min(m, n)
        while i < m and v1[i] == 0:
            i += 1
        
        j = min(m ,n)
        while j < n and v2[j] == 0:
            j += 1
        
        if i < m:
            return 1
        if j < n:
            return -1
        
        return 0

# Solution 2, use zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        v1 = list(map(int, v1))
        v2 = list(map(int, v2))
        
        for a, b in itertools.zip_longest(v1, v2, fillvalue=0):
            if a < b:
                return -1
            if a > b:
                return 1
        
        return 0

# Solution 3, manual zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        m, n = map(len, (v1, v2))
        
        i = 0
        while i < max(m, n):
            a = int(v1[i]) if i < m else 0
            b = int(v2[i]) if i < n else 0
            
            if a < b:
                return -1
            if a > b:
                return 1
            i += 1
        return 0