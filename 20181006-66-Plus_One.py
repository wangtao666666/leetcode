# encoding = 'utf-8'

class Solution(object):
    def plusOne(self,digits):
        """
        :param digits:List[int]
        :return: List[int]
        """
        num = 1

        for i in range(1,len(digits)):
            a = digits[-i] + num
            digits[-i] = a % 10
            num = int(a / 10)

        if num >= 1:
            digits.insert(0,num)

        return digits

digits = [4,3,2,1]
test = Solution()
result = test.plusOne(digits)
print(result)
