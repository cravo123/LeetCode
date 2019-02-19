import collections

class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        d = collections.Counter(moves)
        
        return d['U'] == d['D'] and d['L'] == d['R']