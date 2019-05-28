# Solution 1, stack, greedy
# Find s1, s2, s3 where s1 < s3 < s2. here 1, 2, 3 means position index
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float('-inf')
        q = []
        
        for c in reversed(nums):
            if c < s3:
                return True
            # since c >= s3, so c should be new s2 now
            # we need to update s3 then, s3 will always be larger than before 
            while q and c > q[-1]:
                s3 = q.pop()
            q.append(c)
        return False

# Solution 2, O(n ^ 2)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_min = float('inf')
        
        for i in range(n - 1):
            curr_min = min(curr_min, nums[i])
            if curr_min == nums[i]:
                continue
            
            for j in range(i + 1, n):
                if curr_min < nums[j] < nums[i]:
                    return True
        return False