# encoding = 'utf-8'

class Solution(object):
    def pivotIndex(self,nums):
        """
        :param num:
        :return:
        """
        sum_data = sum(nums)
        sum_left = 0
        for i in range(0,len(nums)):
            sum_data = sum_data - nums[i]

            if sum_data == sum_left:
                return i
            else:
                sum_left += nums[i]

        return -1


nums = [1,7,3,6,5,6]
test = Solution()
result = test.pivotIndex(nums)
print(result)