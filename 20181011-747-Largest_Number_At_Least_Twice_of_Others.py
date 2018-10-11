# encoding = 'utf-8'

class Solution(object):
    def dominantIndex(self,nums):
        """
        :param nums:
        :return:
        """
        max_num = max(nums)
        max_index = nums.index(max_num)
        nums.remove(max_num)

        for a in nums:
            if max_num < 2*a:
                return -1

        return max_index

nums = [3,6,1,0]
test = Solution()
result = test.dominantIndex(nums)
print(result)
