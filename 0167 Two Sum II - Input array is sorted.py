class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        
        while i < j:
            v = numbers[i] + numbers[j]
            if v < target:
                i += 1
            elif v > target:
                j -= 1
            else:
                return [i + 1, j + 1]