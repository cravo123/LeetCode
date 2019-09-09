import bisect

# Solution 1, linear search, O(n)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        
        return letters[0]

# Solution 2, binary search O(logn)
# Whenever input is sorted, you should always think of binary search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        
        return letters[idx % len(letters)]