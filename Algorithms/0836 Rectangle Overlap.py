class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1 = max(rec1[0], rec2[0]), max(rec1[1], rec2[1])
        x2, y2 = min(rec1[2], rec2[2]), min(rec1[3], rec2[3])
        
        if x1 < x2 and y1 < y2:
            return True
        
        return False