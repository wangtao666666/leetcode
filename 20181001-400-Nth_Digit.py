# encoding='utf-9'

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        digit_len = 1
        while n > digit_len * 9 * (10 ** (digit_len-1)):
            n -= digit_len  * 9 * (10 ** (digit_len-1))
            digit_len += 1

        num = 10 ** (digit_len-1) + (n-1)/digit_len

        nth_digit = num / (10 ** ((digit_len-1) - ((n-1)%digit_len)))
        nth_digit %= 10

        return int(nth_digit)

n = 3
test = Solution()
result = test.findNthDigit(n)
print(result)