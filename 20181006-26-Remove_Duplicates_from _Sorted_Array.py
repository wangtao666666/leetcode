# encoding = 'utf-8'

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j = j + 1

            print(nums)
        return j + 1

nums = [1,1,2]
test = Solution()
result = test.removeDuplicates(nums)
print(result)
