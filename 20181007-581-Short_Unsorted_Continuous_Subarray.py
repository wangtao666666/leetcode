# encoding = 'utf-8'

class Solution(object):
    def findUnsortedSubarray(self,nums):
        """
        :param nums:List[int]
        :return: int
        """
        sort = sorted(nums)
        data = []

        for i in range(len(nums)):
            if sort[i]!=nums[i]:
                data.append(i)

        if not data:
            return 0
        else:
            return data[-1] - data[0] + 1

nums = [2,6,4,8,10,9,15]
test = Solution()
result = test.findUnsortedSubarray(nums)
print(result)
