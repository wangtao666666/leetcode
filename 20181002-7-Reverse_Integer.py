# encoding='utf-8'

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        mindata = -pow(2, 31)
        maxdata = pow(2, 31) - 1

        if x < mindata or x > maxdata:
            return 0
        else:
            if x < 0:
                result = -int(str(-x)[::-1])
            else:
                result = int(str(x)[::-1])

        if result < mindata or result > maxdata:
            return 0
        else:
            return result


x = 123
test = Solution()
result = test.reverse(x)
print(result)