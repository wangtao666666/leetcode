# encoding = 'utf-8'

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.strip().split(' ') if i])


s = "Hello, my name is John"
test = Solution()
result = test.countSegments(s)
print(result)

