# encoding = 'utf-8'

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j

nums = [0,1,2,2,3,0,4,2]
# nums = [0,1]
val = 2
test = Solution()
result = test.removeElement(nums,val)
print(result)

