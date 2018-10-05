# encoding='utf-8'

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        """
        三角形计算公式参考链接：https://en.wikipedia.org/wiki/Shoelace_formula
        """

        Area = lambda x1, y1, x2, y2, x3, y3: abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        length = len(points)
        result = 0

        for i in range(length):
            for j in range(i + 1, length):
                for z in range(j + 1, length):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[z]

                    result = max(result, Area(x1, y1, x2, y2, x3, y3))

        return result

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
test = Solution()
result = test.largestTriangleArea(points)
print(result)
