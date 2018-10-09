# encoding = 'utf-8'

class Solution(object):
    def findLengthOfLCIS(self,nums):
        """
        :param nums:
        :return:
        """
        a = 0
        b = 0

        for i in range(len(nums)):
            if i==0 or nums[i-1] < nums[i]:
                b +=1
                a = max(a,b)
            else:
                b = 1

        return a


nums = [1,3,5,4,7]
test = Solution()
result = test.findLengthOfLCIS(nums)
print(result)

