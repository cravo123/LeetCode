# Solution 1, simulation
# First count how many rows we need, and then fill
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        left, right = 0, candies
        while left < right:
            mid = (left + right) // 2
            v = (1 + mid) * mid // 2
            if v < candies:
                left = mid + 1
            else:
                right = mid
        
        cnt = (left - 1) // num_people
        
        res = [(i + i + num_people * (cnt - 1)) * cnt // 2 for i in range(1, num_people + 1)]
        
        v = candies - sum(res)
        i = 0
        while v > 0:
            x = min(v, cnt * num_people + i + 1)
            v -= x
            res[i] += x
            i += 1
        
        return res

# Solution 2, simple simulation
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for _ in range(num_people)]
        i, n = 1, num_people
        v = candies
        
        while v > 0:
            x = min(v, i)
            v -= x
            res[(i - 1) % n] += x
            i += 1
        
        return res