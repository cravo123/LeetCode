import collections

# Solution 1, hashset
# We can switch values at any two indices i and j (i < j) by using reverse operations below,
#   step 1, reverse A[i:(j + 1)],
#   step 2, reverse A[(i + 1):j]
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = collections.Counter(target)
        
        for c in arr:
            d[c] -= 1
            if d[c] < 0:
                return False
        return True