# encoding = 'utf-8'

class Solution(object):
    def rotate(self,nums,k):
        """
        :param num:List[int]
        :param k: int
        :return:
        """

        k = k % len(nums)

        nums[:k],nums[k:] = nums[len(nums)-k:],nums[:,len(nums)-k]
