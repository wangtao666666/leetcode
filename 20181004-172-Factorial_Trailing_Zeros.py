class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        n = a * 10^K = a * (5^k * 2^k)
        5,10,15,20,25,30
        
        """
        res = 0

        while n > 0:
            res = res + n / 5
            n = n / 5

        return res

n = 10
test = Solution()
result = test.trailingZeroes(n)
print(result)
