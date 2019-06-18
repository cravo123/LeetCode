# Solution 1, simulation
# using temp list to store result, and then copy back
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        q = []
        n = len(arr)
        
        for c in arr:
            q.append(c)
            if c == 0:
                q.append(c)
            
            if len(q) >= n:
                break
        
        for i in range(n):
            arr[i] = q[i]

# Solution 2, two-pass O(1) memory
# t.b.c