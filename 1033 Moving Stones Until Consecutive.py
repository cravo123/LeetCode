# Edge Cases
#  1, 2, 3,   consecutive sequence, return 0, 0
#  1, 2, 6 or 1, 3, 6, min should be 1
#  Otherwise, min is 2

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x = [a, b, c]
        x.sort()
        a, b, c = x
        
        v1 = b - a
        v2 = c - b
        
        v_min = min(v1, v2)
        v_max = max(v1, v2)
        
        if v_min == v_max == 1:
            return [0, 0]
        if v_min <= 2:
            return [1, v_min + v_max - 2]
        
        return [2, v_min + v_max - 2]