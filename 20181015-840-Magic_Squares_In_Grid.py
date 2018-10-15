# encoding = 'utf-8'

"""
    参考连接：https://blog.csdn.net/fuxuemingzhu/article/details/80473253
"""
class Solution(object):
    def numMagicSquaresInside(self,grid):
        """
        :param grid:
        :return:
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        count = 0

        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                matrix = [[grid[row+i][col + j] for j in range(3)] for i in range(3)]
                if self.magic(matrix):
                    count +=1

        return count

    def magic(self,matrix):
        number = all(1<=matrix[i][j] for i in range(3) for j in range(3))
        row = all(sum(rows) == 15 for rows in matrix)
        col = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        diagonal = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0]==10

        return number and row and col and diagonal

matrix = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
test = Solution()
result = test.numMagicSquaresInside(matrix)
print(result)
