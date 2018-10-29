# encoding = 'utf-8'

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = s[1:] + s[:-1]

        return (tmp.find(s) != -1)





s = 'abab'
test = Solution()
result = test.repeatedSubstringPattern(s)
print(result)
