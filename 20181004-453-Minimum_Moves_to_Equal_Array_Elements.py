# encoding='utf-8'

"""
 思路解析参考链接：https://blog.csdn.net/weixin_41362649/article/details/79915371
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums)*len(nums)

nums = [1,2,3]
test = Solution()
result = test.minMoves(nums)
print(result)