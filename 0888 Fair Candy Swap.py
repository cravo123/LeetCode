class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        need = (sum(A) + sum(B)) // 2
        a_miss = need - sum(A)
        B = set(B)
        for v in A:
            if v + a_miss in B:
                return [v, v + a_miss]