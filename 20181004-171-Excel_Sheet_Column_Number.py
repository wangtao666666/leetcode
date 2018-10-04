#encoding='utf-8'

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for a in s:
            res = res*26 + (ord(a)-64)

        return res


s = 'A'
test = Solution()
result = test.titleToNumber(s)
print(result)