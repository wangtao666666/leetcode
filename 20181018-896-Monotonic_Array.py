# encoding = 'utf-8'

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A == sorted(A) or A == sorted(A)[::-1]


A = [1,2,2,3]
test = Solution()
result = test.isMonotonic(A)
print(result)
