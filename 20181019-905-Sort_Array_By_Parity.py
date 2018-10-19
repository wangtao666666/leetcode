# encoding = 'utf-8'

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        oed = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                oed.append(A[i])
            else:
                odd.append(A[i])

        return oed + odd


A = [3,1,2,4]
test = Solution()
result = test.sortArrayByParity(A)
print(result)
