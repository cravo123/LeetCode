import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        # zero
        # one
        # two
        # three
        # four
        # five
        # six
        # seven
        # eight
        # nine
        
        # 0: #z
        # 2: #w
        # 4: #u
        # 6: #x
        # 8: #g
        # 3: #h - #8
        # 5: #f - #4
        # 7: #s - #6
        # 1: #o - #0 - #2 - #4
        # 9: (#n - #1 - #7) // 2
        
        d = collections.Counter(s)
        res = {}
        res['0'] = d['z']
        res['2'] = d['w']
        res['4'] = d['u']
        res['6'] = d['x']
        res['8'] = d['g']
        res['3'] = d['h'] - res['8']
        res['5'] = d['f'] - res['4']
        res['7'] = d['s'] - res['6']
        res['1'] = d['o'] - res['0'] - res['2'] - res['4']
        res['9'] = (d['n'] - res['1'] - res['7']) // 2
        
        res = [c * v for c, v in res.items()]
        res = ''.join(res)
        res = ''.join(list(sorted(res)))
        
        return res