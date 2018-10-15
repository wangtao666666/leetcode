# encoding = 'utf-8'

class Solution(object):
    def flipAndInvertImage(self,A):
        """
        :param A:
        :return:
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]

        for i in range(len(A)):
            A[i] = [1 if x==0 else 0 for x in A[i]]

        return A


A = [[1,1,0],[1,0,1],[0,0,0]]
test = Solution()
result = test.flipAndInvertImage(A)
print(result)
