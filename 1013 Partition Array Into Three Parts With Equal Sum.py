import collections

# Solution 1, more elegant
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        
        if total % 3 != 0:
            return False
        
        target = total // 3
        curr = 0
        cnt = 0
        
        for c in A:
            curr += c
            if curr == target:
                cnt += 1
                curr = 0
            if cnt == 3:
                return True
        return False

# Solution 2, two pointers
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        
        if total % 3 != 0:
            return False
        target = total // 3
        
        n = len(A)
        
        left_sum = right_sum = 0
        i, j = 0, n - 1
        while i < j:
            while i < j and left_sum != target:
                left_sum += A[i]
                i += 1
            
            while i < j and right_sum != target:
                right_sum += A[j]
                j -= 1
            
            if 0 < i <= j < n - 1 and left_sum == right_sum and left_sum == target:
                return True
        
        return False

# Solution 3, hash-table
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        
        if total % 3 != 0:
            return False
        target = total // 3
        
        d = collections.defaultdict(set)
        curr = 0
        
        for i, c in enumerate(A):
            curr += c
            d[curr].add(i)
        
        if target in d and target * 2 in d:
            for i in d[target]:
                for j in d[target * 2]:
                    if i < j:
                        return True
        
        return False
