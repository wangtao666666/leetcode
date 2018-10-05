# encoding='utf-8'

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        length = int(math.sqrt(c))

        for a in range(length + 1):
            b = c - a * a

            if int(math.sqrt(b)) ** 2 == b:
                return True

        return False

c = 5
test = Solution()
result = test.judgeSquareSum(c)
print(result)

