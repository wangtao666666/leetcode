# encoding = 'utf-8'

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1

        return haystack.index(needle)



haystack = 'hello'
needle = 'll'
test = Solution()
result = test.strStr(haystack,needle)
print(result)