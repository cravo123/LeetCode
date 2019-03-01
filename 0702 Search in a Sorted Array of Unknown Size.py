class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i = 1
        
        while True:
            val = reader.get(i)
            
            if val >= target:
                break
            i *= 2
        
        left, right = 0, i
        
        while left < right:
            mid = (left + right) // 2
            val = reader.get(mid)
            
            if val < target:
                left = mid + 1
            else:
                right = mid
        
        return left if reader.get(left) == target else -1