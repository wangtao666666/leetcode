# encoding = 'utf-8'

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m * n

        min_1 = ops[0][0]
        min_2 = ops[0][1]
        for i in range(1, len(ops)):
            if ops[i][0] < min_1:
                min_1 = ops[i][0]

            if ops[i][1] < min_2:
                min_2 = ops[i][1]

        return min_1 * min_2

m = 3
n = 3
ops = [[2,2],[3,3]]
test = Solution()
result = test.maxCount(m,n,ops)
print(result)
