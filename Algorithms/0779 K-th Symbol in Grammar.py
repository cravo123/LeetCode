# Solution 1, recursion. View it as a binary tree
#   0         1
#  / \       / \
# 0   1     1   0
class Solution(object):
    def dfs(self, row, cnt):
        if row == 0:
            return 0
        
        if cnt % 2 == 0:
            # left child
            if self.dfs(row - 1, cnt // 2) == 0:
                return 0
            else:
                return 1
        else:
            # right child
            if self.dfs(row - 1, cnt // 2) == 0:
                return 1
            else:
                return 0
        
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return self.dfs(N, K - 1)

# Could simplify logic to be
class Solution(object):
    def dfs(self, row, cnt):
        if row == 0:
            return 0
        
        v = self.dfs(row - 1, cnt // 2)
        
        if cnt % 2 == v:
            return 0
        return 1
           
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return self.dfs(N, K - 1)


# Solution 2, naive find invariant, second half is flipped from first half
# so we use flag to count how many flips we have done
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        n = N
        k = K - 1
        
        v = int(2 ** (n - 2))
        flag = 0
        while n > 1 and k > 0:
            if k >= v:
                k -= v
                flag = 1 - flag
            v //= 2
            n -= 1
        
        return 0 if flag == 0 else 1