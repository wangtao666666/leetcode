# encoding = 'utf-8'

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1

        return max(len(a), len(b))


a = 'aba'
b = 'cdc'
test = Solution()
result = test.findLUSlength(a,b)
print(result)