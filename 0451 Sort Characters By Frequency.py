class Solution:
    def frequencySort(self, s: 'str') -> 'str':
        s = list(s)
        
        d = collections.Counter(s)
        
        s.sort(key=lambda c: [-d[c], c])
        s = ''.join(s)
        
        return s
