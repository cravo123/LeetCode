# Solution 1, similar to 2-sum
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        
        for v in arr:
            if 2 * v in d or (v % 2 == 0 and v // 2 in d):
                return True
            d.add(v)
        
        return False