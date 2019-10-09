# Solution 1, simulation
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        # since we can move 2 units left or right for a cost of 0
        # then all odd and even numbers form equivalence class respectively
        odd = sum(c % 2 for c in chips)
        even = sum(1 if c % 2 == 0 else 0 for c in chips)
        
        return min(odd, even)