class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A:
            return 0
        res = sum(1 if list(row) != sorted(row) else 0 for row in zip(*A))
        
        return res