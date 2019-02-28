class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if not S:
            return [0, 0]
        res = 0
        curr = 0
        max_len = 100
        for c in S:
            new_width = widths[ord(c) - ord('a')]
            if curr + new_width > max_len:
                res += 1
                curr = new_width
            else:
                curr += new_width
        return [res + 1, curr]