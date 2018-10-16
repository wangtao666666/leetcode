# encoding = 'utf-8'

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)

A = [[1,2,3],[4,5,6]]
test = Solution()
result = test.transpose(A)
print(result)
