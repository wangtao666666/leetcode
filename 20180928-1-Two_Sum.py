# encoding='utf-8'

"""
    Question 1:Two Sum
    Description:给定一个整数列表，返回两个数字的索引，使它们相加得到特定目标
    @author:wt
    Created at 2018-09-28

    example:
        nums = [2,7,11,15],target = 9
    由于 nums[0] + nums[1] = 2 + 7 = 9
    return [0,1]

"""

class Solution(object):
    def twoSum(self,nums,target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        # method1:暴力双重for循环

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i,j]

        # method2：两层for循环，筛选掉一些不必要的比较

        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]


        #method3:一层循环，先找一个值之后差值在列表中查询

        l = len(nums)
        for i in range(l):
            a = nums[i]
            other = target - a
            if other in nums:
                j = nums.index(other)
                if i!=j:
                    if i>j:
                        return [j,i]
                    return [i,j]

        #method4:一层for循环优化，转换字典形式

        l = len(nums)
        dict_nums = {nums[i]:i for i in range(l)}
        for i in range(l):
            num = nums[i]
            other = target - num
            if other in dict_nums and i!=dict_nums[other]:
                return [i,dict_nums[other]]

nums = [2,7,11,15]
target = 9
test = Solution()
result = test.twoSum(nums=nums,target=target)
print(result)

"""
Conclusion:字典变量要比列表遍历快很多，但是生成字典比生成列表慢
"""


