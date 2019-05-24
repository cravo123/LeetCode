# Solution 1, similar to LC 0031 Next Permutation 
# and LC 0556

class Solution:
    def maximumSwap(self, num: int) -> int:
        d = {}
        num = list(str(num))
        n = len(num)
        
        i = 0
        while i < n - 1:
            if num[i] < num[i + 1]:
                break
            i += 1
        
        if i == n - 1:
            return int(''.join(num))
        
        v = max(num[(i + 1):])
        j = n - 1
        while j > i and num[j] != v:
            j -= 1
        
        k = 0
        while k < i and num[k] >= v:
            k += 1
        num[k], num[j] = num[j], num[k]
        
        return int(''.join(num))