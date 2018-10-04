# encoding='utf-8'

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method1

        #         import math

        #         if n <= 0:
        #             return False

        #         max_data = 2**31 - 1
        #         k = math.log(max_data)/math.log(3)
        #         k = math.floor(k)
        #         big3 = math.pow(3,k)

        #         return (big3%n==0)

        # mehtod2

        while n > 0 and n % 3 == 0:
            n = n / 3

        return n == 1

n = 10
test = Solution()
result = test.isPowerOfThree(n)
print(result)