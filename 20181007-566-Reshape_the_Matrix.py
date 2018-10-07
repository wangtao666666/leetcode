# encoding = 'utf-8'

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        data = []
        for a in nums:
            data = data + a

        if r * c != len(data):
            return nums

        result = []
        for i in range(int(len(data) / c)):
            result.append(data[i * c:(i + 1) * c])

        return result

nums = [[1,2],[3,4]]
r = 1
c = 4
test = Solution()
result = test.matrixReshape(nums,r,c)
print(result)
