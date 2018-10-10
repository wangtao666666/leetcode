# encoding = 'utf-8'

"""
参考连接：https://blog.csdn.net/Chris_zhangrx/article/details/78955171
"""
class Solution(object):
    def findShortestSubArray(self,nums):
        """
        :param num:
        :return:
        """
        from collections import Counter,defaultdict

        degree  = max(Counter(nums).values())
        so_far = defaultdict(int)
        min_size = len(nums)
        start,end = 0,len(nums) - 1

        for end,num in enumerate(nums):
            so_far[num] +=1
            while start <= end and so_far[num] == degree:
                min_size = min(min_size,end-start+1)
                so_far[nums[start]] -= 1
                start +=1

        return min_size

nums = [1,2,2,3,1]

test = Solution()
result = test.findShortestSubArray(nums)
print(result)
