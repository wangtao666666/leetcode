# encoding = 'utf-8'

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = [c for c in s.lower() if c.isalnum()]
        return d == d[::-1]


s = 'OP'
test = Solution()
result = test.isPalindrome(s)
print(result)