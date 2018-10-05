# encoding = 'utf-8'

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        """
        思想和之前算算区域面积那道题一样，看两个图是否有交集
        """
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
test = Solution()
result = test.isRectangleOverlap(rec1,rec2)
print(result)
