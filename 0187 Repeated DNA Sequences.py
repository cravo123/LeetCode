import collections

# Solution 1, O(k * n), not efficient
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = collections.Counter()
        
        n = len(s)
        res = []
        for i in range(n - 9):
            tmp = s[i:(i + 10)]
            d[tmp] += 1
            
            if d[tmp] == 2:
                res.append(tmp)
        
        return res

# Solution 2, Rabin–Karp algorithm, rolling hash-value
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        
        d = collections.defaultdict(set) # hash-val: string
        
        base = int(10 ** 5 + 7) # better be big prime
               
        i = 0
        curr = 0
        
        while i < 10:
            curr = curr * 4 + ord(s[i]) - ord('A')
            i += 1
        curr %= base
        
        d[curr].add(s[:10])
        res = set()
        
        for i in range(10, n):
            curr = curr * 4 - (ord(s[i - 10]) - ord('A')) * int(4 ** 10) + ord(s[i]) - ord('A')
            curr = (curr + base) % base
            t = s[(i - 9):(i + 1)]
            if t in d[curr] and t not in res:
                res.add(t)
            d[curr].add(t)
        
        res = list(res)
        
        return res