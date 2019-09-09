# Solution 1, plain sort
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [a * x * x + b * x + c for x in nums]
        res.sort()
        
        return res

# Solution 2, use the condition that nums are sorted
# Two pointers, but it calculates quadratic function f value
# Instead, we can use distance to central point from middle school 
# to determine which x will generate larger f value
class Solution:
    def f(self, x, a, b, c):
        return a * x * x + b * x + c
        
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        i, j = 0, len(nums) - 1
        
        res = [0 for _ in nums]
        
        if a >= 0:
            idx = len(nums) - 1
        else:
            idx = 0
        
        while i <= j:
            v_i, v_j = self.f(nums[i], a, b, c), self.f(nums[j], a, b, c)
            
            if a >= 0:                
                if v_i >= v_j:
                    res[idx] = v_i
                    i += 1
                else:
                    res[idx] = v_j
                    j -= 1
                idx -= 1
            else:
                if v_i < v_j:
                    res[idx] = v_i
                    i += 1
                else:
                    res[idx] = v_j
                    j -= 1
                idx += 1
        return res

# Solution 2.1,
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            # line
            if b >= 0:
                res = nums
            else:
                res = nums[::-1]
        else:
            # quadratic
            v = -b / (2 * a)

            res = nums[::]
            idx = len(res) - 1

            i, j = 0, len(nums) - 1

            while i <= j:
                if abs(nums[i] - v) > abs(nums[j] - v):
                    res[idx] = nums[i]
                    i += 1
                else:
                    res[idx] = nums[j]
                    j -= 1
                idx -= 1
            if a < 0:
                res = res[::-1]
        
        res = [a * x * x + b * x + c for x in res]
        
        return res
            
