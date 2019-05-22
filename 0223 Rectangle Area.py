class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        bottom_left = max(A, E), max(B, F)
        top_right = min(C, G), min(D, H)
        
        length = top_right[0] - bottom_left[0]
        height = top_right[1] - bottom_left[1]
        
        if length < 0 and height < 0:
            overlap = 0
        else:
            overlap = max(0, length * height)
        
        total = (C - A) * (D - B) + (G - E) * (H - F)
        
        return total - overlap