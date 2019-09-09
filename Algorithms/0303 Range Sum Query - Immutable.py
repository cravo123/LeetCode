class NumArray:

    def __init__(self, nums: List[int]):
        q = [0]
        curr = 0
        for c in nums:
            curr += c
            q.append(curr)
        self.q = q

    def sumRange(self, i: int, j: int) -> int:
        return self.q[j + 1] - self.q[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)