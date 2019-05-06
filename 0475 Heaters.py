import bisect

# Solution 1, binary search
# O(Houses * log Heaters)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        res = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            if idx == 0:
                dist = heaters[0] - house
            elif idx == len(heaters):
                dist = house - heaters[-1]
            else:
                dist = min(house - heaters[idx - 1], heaters[idx] - house)
            res = max(res, dist)
        
        return res

# Solution 2, two pointers
# O(Houses log Houses + Heaters log Heaters)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        i, n = 0, len(heaters)
        res = 0
        for house in houses:
            # gotcha, need = sign
            # this is for cases where there are duplicates in heaters....
            while i < n - 1 and abs(heaters[i] - house) >= abs(heaters[i + 1] - house): 
                i += 1
            res = max(res, abs(heaters[i] - house))
        
        return res