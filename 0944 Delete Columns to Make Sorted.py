# Solution 1, simulation
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A:
            return 0
        res = sum(1 if list(row) != sorted(row) else 0 for row in zip(*A))
        
        return res

# Solution 2, manual check
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        A = list(zip(*A))
        
        res = 0
        for row in A:
            for i in range(1, len(row)):
                if row[i] < row[i - 1]:
                    res += 1
                    break
        return res