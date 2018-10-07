# encoding = 'utf-8'

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n -=1

        return n<=0

flowerbed = [1,0,0,0,0,1]
n = 2

test = Solution()
result = test.canPlaceFlowers(flowerbed,n)
print(result)
