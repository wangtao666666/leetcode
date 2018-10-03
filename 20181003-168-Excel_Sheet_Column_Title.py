class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:

            res = chr((n - 1) % 26 + 65) + res

            n = int((n - 1) / 26)

        return res


ss = 28

test = Solution()
result = test.convertToTitle(ss)

print(result)

