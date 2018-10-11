# encoding = 'utf-8'

class Solution(object):
    def isToeplitzMatrix(self,matrix):
        """
        :param matrix:
        :return:
        """

        # row = len(matrix)
        #
        # for i in range(row-1):
        #     if matrix[i][i:len(matrix[0])-(i+2)] != matrix[i+1][i+1:len(matrix[0])-(i+2)]:
        #         print(i)
        #         return False
        #
        # return True

        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
test = Solution()
result = test.isToeplitzMatrix(matrix)
print(result)
