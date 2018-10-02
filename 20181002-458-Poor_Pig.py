# encoding = 'utf-8'


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0

        while (pow(minutesToTest / minutesToDie + 1, pigs) < buckets):
            pigs += 1

        return pigs

buckets = 1000
minutersToDie = 15
minutesToTest = 60

test = Solution()
result = test.poorPigs(buckets,minutersToDie,minutesToTest)
print(result)
