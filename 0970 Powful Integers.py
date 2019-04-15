import math
# Solution 1, brute force, but not elegant
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            return [2] if bound >= 2 else []
        
        if x == 1 or y == 1:
            v = max(x, y)
            res = []
            
            curr = 1
            while curr + 1 <= bound:
                res.append(curr + 1)
                curr *= v
            return res
        
        m = int(math.log(bound) / math.log(x) + 1)
        n = int(math.log(bound) / math.log(y) + 1)
        
        res = set()
        for i in range(m):
            for j in range(n):
                v = int(x ** i) + int(y ** j)
                if v <= bound:
                    res.add(v)
        res = list(res)
        
        return res

# Solution 2, same brute force but elegant
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        i = j = 0
        curr_x = 1
        while curr_x < bound:
            curr_y = 1
            while curr_x + curr_y <= bound:
                res.add(curr_x + curr_y)
                curr_y *= y
                
                if curr_y == 1:
                    break
            curr_x *= x
            
            if curr_x == 1:
                break
        
        res = list(res)
        
        return res