# Solution 1, stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for c in tokens:
            if c not in '+-*/':
                nums.append(int(c))
            else:
                second, first = nums.pop(), nums.pop()
                if c == '+':
                    nums.append(first + second)
                elif c == '-':
                    nums.append(first - second)
                elif c == '*':
                    nums.append(first * second)
                else:
                    flag = -1 if first * second < 0 else 1
                    nums.append(abs(first) // abs(second) * flag)

                    # this is much more elegant
                    # nums.append(int(first / second))
        return nums[0]