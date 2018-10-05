# encoding='utf-8'

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_1 = 0
        num_2 = 0
        num_3 = 0
        num = 0


        for i in range(len(grid)):
            l = []
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    num_1 += 1
                l.append(grid[j][i])
            num = max(l)

            num_3 = num_3 + num

            num_2 = num_2 + max(grid[i])
        # print('num_1:',num_1)
        # print('num_2:',num_2)
        # print('num_3:',num_3)

        return num_1 + num_2 + num_3

grid = [[1,0],[5,4]]
test = Solution()
result = test.projectionArea(grid)
print(result)
