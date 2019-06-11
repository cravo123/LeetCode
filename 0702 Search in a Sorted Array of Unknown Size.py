# Solution 1, binary search
# First double search size if current val is smaller than target
# Then when we break, we know our search range is (j // 2, j)
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        j = 1
        
        while reader.get(j) < target:
            j *= 2
        
        i = j // 2
        
        while i < j:
            m = (i + j) // 2
            
            v = reader.get(m)
            
            if v < target:
                i = m + 1
            else:
                j = m
        
        return i if reader.get(i) == target else -1