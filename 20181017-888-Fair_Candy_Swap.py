# encoding = 'utf-8'

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        """
        
        sum(A) - x + y = sum(B) + x - y
        y = (sum(A)+sum(B))/2 + x
         
        """
        totalA, totalB, setB = sum(A), sum(B), set(B)

        for a in A:
            if (totalB - totalA) // 2 + a in setB:
                return [a, (totalB - totalA) // 2 + a]

A = [1,1]
B = [2,2]

test = Solution()
result = test.fairCandySwap(A,B)
print(result)

