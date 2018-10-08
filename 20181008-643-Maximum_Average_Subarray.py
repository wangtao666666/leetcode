# encoding = 'utf-8'

class Solution(object):
    def findMaxAverage(self,nums,k):
        """
        :param nums:
        :param k:
        :return:
        """
        ans = 0
        res = 0

        for i in range(len(nums)):
            res += nums[i]
            if i>=k:
                res -=nums[i-k]

            print('res:',res)

            if i>=k-1:
                ans = max(ans,res/k)

            print('ans:',ans)

        return ans



# nums = [1,12,-5,-6,50,3]
nums = [0,1,1,3,3]
k = 4
test = Solution()
result = test.findMaxAverage(nums,k)
print(result)
