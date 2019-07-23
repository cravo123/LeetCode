# Solution 1, Greedy, sorting
# Idea is that company either needs to pay price_A or price_B
# So sending candidate to A instead of B will need (price_A - price_B) more money (could be negative)
# Need to minimize total cost of this.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)
        res = sum(c[0] if i < n // 2 else c[1] for i, c in enumerate(costs))
        
        return res