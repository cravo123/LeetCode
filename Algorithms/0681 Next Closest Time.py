# Solution 1, back-tracking
class Solution:
    def diff(self, curr, target):
        if curr > target:
            return curr - target
        return 24 * 60 - (target - curr)
    
    def dfs(self, path, digits, target):
        if len(path) == 2:
            t = path[0] * 10 + path[1]
            if t > 23:
                return
        
        if len(path) == 4:
            t = path[2] * 10 + path[3] 
            # gotcha, need to check correctness for hour and minute
            if t > 59:
                return
            t += (path[0] * 10 + path[1]) * 60
            curr_diff = self.diff(t, target)
            
            if 0 < curr_diff < self.diff(self.res, target):
                self.res = t
            return
        
        for v in digits:
            path.append(v)
            self.dfs(path, digits, target)
            path.pop()
        
    def nextClosestTime(self, time: str) -> str:
        self.res = float('inf')
        
        digits = set(time)
        digits.discard(':')
        digits = list(int(c) for c in digits)
        
        path = []
        target = int(time[:2]) * 60 + int(time[3:])
        self.dfs(path, digits, target)
        
        res = '%02d:%02d' % (self.res // 60, self.res % 60)
        
        return res

# Solution 2, enumerate all times after current time
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time)
        
        curr = int(time[:2]) * 60 + int(time[3:])
        
        while True:
            curr = (curr + 1) % (24 * 60)
            h = '%02d' % (curr // 60)
            m = '%02d' % (curr % 60)
            
            cs = set(h + m)
            
            if all(c in digits for c in cs):
                return h + ':' + m
