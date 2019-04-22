import functools

# Solution 1, customized comparator for sorting
# Similar to LC 1029
def customized_cmp(a, b):
    a, b = map(str, (a, b))    
    return int(b + a) - int(a + b)
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums.sort(key=functools.cmp_to_key(customized_cmp))
        
        return str(int(''.join(nums)))