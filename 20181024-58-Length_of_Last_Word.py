# encoding = 'utf-8'

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])



s = 'Hello World'
test = Solution()
result = test.lengthOfLastWord(s)
print(result)
