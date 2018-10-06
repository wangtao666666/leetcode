# encoding = 'utf-8'

class Solution(object):
    def maxProfit(self,prices):
        """
        :param prices: List[int]
        :return: int
        """

        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit +=prices[i] - prices[i-1]

        return max_profit

prices = [7,6,4,3,1]
test = Solution()
result = test.maxProfit(prices)
print(result)
