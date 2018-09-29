# encoding='utf-8'

"""
    Question 4:Median of Two Sorted Arrays
    Description:有两个排序的列表nums1和nums2分别为m和n，找到两个排序数组额中位数，总运行时间发杂读为O(log(m+n)),可以假设nums1和nums2不能都为空
    @author:wt
    Created at 2018-09-29

    example1:
        nums1 = [1,3]
        nums2 = [2]

        return 2.0

    example2:
        nums1 = [1,2]
        nums2 = [3,4]

        return （2+3）／2 ＝ 2.5


"""
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :param nums1:List[int]
        :param nums2:List[int]
        :return:float
        """

    #method1:两个列表拼接、排序，算出列表的长度，判断奇偶，测出中位数下标，求出中位数

        nums = nums1 + nums2
        nums.sort()
        l = len(nums)

        if l%2 == 0:
            index = [l//2 - 1,l//2]
        else:
            index = [l//2,l//2]

        median_num = (nums[index[0]]+nums[index[1]])/2.0

        return median_num




nums1 = [1,3]
nums2 = [2]

test = Solution()
result = test.findMedianSortedArrays(nums1=nums1,nums2=nums2)
print(result)