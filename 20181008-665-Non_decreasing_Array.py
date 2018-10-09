# encoding = 'utf-8'

class Solution(object):
    def checkPossibility(self,nums):
        """
        :param nums:
        :return:
        """

        if len(nums) < 2:
            return True

        a1 = nums[:]
        a2 = nums[:]

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a1[i] = nums[i+1]
                a2[i+1] = nums[i]
                break

        return sorted(a1)==a1 or sorted(a2)==a2

nums = [4,2,3]
test = Solution()
result = test.checkPossibility(nums)
print(result)
