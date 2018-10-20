# encoding = 'utf-8'

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        odd = []
        even = []

        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        result = []
        m = 0
        n = 0
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even[m])
                m += 1
            else:
                result.append(odd[n])
                n += 1

        return result

A = [4,2,5,7]
test = Solution()
result = test.sortArrayByParityII(A)
print(result)


