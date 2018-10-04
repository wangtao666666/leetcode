# encoding='utf-8'

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        ab = a*10 + b
        ab％9 ＝ (a*9 + a + b)%9 = (a+b)%9
        abc = a*100 + b*10 + c
        abc = (a*99 + b*9 + c)%9 = (a+b+c)%9
        [0-8] - >[1-9] 
        """
        if num <= 0 :
            return 0
        else:
            return ((num-1)%9+1)


num = 38

test = Solution()
result = test.addDigits(num)
print(result)