class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        res_idx = float('inf')
        
        d = {v:i for i, v in enumerate(list1)}
        
        for i, c in enumerate(list2):
            if c in d:
                if d[c] + i == res_idx:
                    res.append(c)
                elif d[c] + i < res_idx:
                    res = [c]
                    res_idx = d[c] + i
        return res