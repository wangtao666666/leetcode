# encoding = 'utf-8'

class Solution(object):
    def thirdMax(self,nums):
        """
        :param nums:List[int]
        :return: int
        """

        if len(set(nums)) < 3:
            return max(nums)

        return  sorted(list(set(nums)))[-3]


nums = [2,2,3,1]
test = Solution()
result = test.thirdMax(nums)
print(result)