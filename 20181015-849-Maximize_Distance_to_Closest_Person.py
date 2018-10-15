# encoding = 'utf-8'

"""
    参考链接：https://leetcode.com/problems/maximize-distance-to-closest-person/description/
"""
class Solution(object):
    def maxDistToClosest(self,seats):
        """
        :param seats:
        :return:
        """
        prev,result = -1,1

        for i in range(len(seats)):
            if seats[i]:
                if prev<0:
                    result = i
                else:
                    result = max(result,(i-prev)//2)

                prev = i

        return max(result,len(seats)-1-prev)


seats = [1,0,0,0,1,0,1]
test = Solution()
result = test.maxDistToClosest(seats)
print(result)