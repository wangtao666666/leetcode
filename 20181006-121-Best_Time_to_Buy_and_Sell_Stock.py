# encoding = 'utf-8'

class Solution(object):
    def maxProfit(self,prices):
        """
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0

        buy_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            buy_price = min(buy_price,prices[i])
            max_profit = max(max_profit,prices[i]-buy_price)

        return max_profit

prices = [7,1,5,3,6,4]
test = Solution()
result = test.maxProfit(prices)
print(result)