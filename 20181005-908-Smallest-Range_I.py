# encoding = 'utf-8'

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - K - (min(A) + K),0)

A = [0,10]
K = 2

test = Solution()
result = test.smallestRangeI(A,K)
print(result)