# encoding = 'utf-8'

class Solution(object):
    def findDisappearedNumbers(self,nums):
        """
        :param nums:
        :return:
        """
        num = set(nums)
        result = []

        for i in range(1,len(nums)+1):
            if i not in num:
                result.append(i)

        return result

nums = [4,3,2,7,8,2,3,1]
test = Solution()
result = test.findDisappearedNumbers(nums)
print(result)
