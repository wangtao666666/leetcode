# encoding = 'utf-8'

class Solution(object):
    def majorityElement(self,nums):
        """
        :param nums: List[int]
        :return: int
        """

        result = {}
        nums1 = list(set(nums))

        for a in nums1:
            result[a] = nums.count(a)

        result = sorted(result.items(),key=lambda d:d[1],reverse=True)

        return result[0][0]

nums = [2,2,1,1,1,2,2]
test = Solution()
result = test.majorityElement(nums)
print(result)