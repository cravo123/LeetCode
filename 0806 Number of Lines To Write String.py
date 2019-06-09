# Solution 1, simulation
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if not S:
            return [0, 0]
        
        # char: width
        d = {chr(i + ord('a')):v for i, v in enumerate(widths)}
        
        lines, curr = 1, 0
        
        for c in S:
            if d[c] > 100:
                return False
            if curr + d[c] <= 100:
                curr += d[c]
            else:
                lines += 1
                curr = d[c]
        return [lines, curr]