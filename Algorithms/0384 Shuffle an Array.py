import random

# Solution 1, generate random number list and sort it
# Use sorting index to shuffle array
# Random permutation by sorting
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.q = nums[::]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.q = self.nums[::]
        return self.q

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = [[random.random(), i] for i, _ in enumerate(self.q)]
        tmp.sort()
        
        res = self.nums[::]
        
        for i, (v, j) in enumerate(tmp):
            res[i] = self.q[j]
        self.q = res
        
        return self.q

# Solution 2, Fisher–Yates shuffle or (Knuth shuffle)
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums[::]
        self.q = nums[::]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.q = self.nums[::]
        return self.q

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.q)
        
        for i in range(n):
            j = random.randrange(i, n)
            self.q[i], self.q[j] = self.q[j], self.q[i]
        return self.q

# Solution 3, use built-in
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums[::]
        self.q = nums[::]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.q = self.nums[::]
        return self.q
        
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.q[::]
        random.shuffle(res)
        #res = random.sample(self.q, len(self.q))
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()