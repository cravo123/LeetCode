import collections

# Solution 1, cache xs and use set intersection operation
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ys = collections.defaultdict(set)
        
        for x, y in points:
            ys[y].add(x)
        
        res = float('inf')
        
        for y1 in ys:
            for y2 in ys:
                if y2 >= y1:
                    continue
                xs = ys[y1] & ys[y2]
                
                for x1 in xs:
                    for x2 in xs:
                        if x2 >= x1:
                            continue
                        res = min(res, (x1 - x2) * (y1 - y2))
        
        return res if res < float('inf') else 0