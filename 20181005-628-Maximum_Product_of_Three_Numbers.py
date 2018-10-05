# encoding='utf-8'

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return nums[0] * nums[1] * nums[2]

        nums = sorted(nums)

        res1 = nums[0] * nums[1] * nums[-1]
        res2 = nums[-1] * nums[-2] * nums[-3]

        if res1 > res2:
            return res1
        else:
            return res2

nums = [1,2,3,4]
test = Solution()
result = test.maximumProduct(nums)
print(result)