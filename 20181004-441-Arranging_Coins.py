# encoding='utf-8'

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        思想：等差数列求和
        """

        if n == 1:
            return 1

        k = 1
        while k * (k + 1) <= 2 * n:
            k += 1

        return k - 1

n = 100
test = Solution()
result = test.arrangeCoins(n)
print(result)
