# encoding = 'utf-8'

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # return str(int(num1.strip()) + int(num2.strip()))
        return str(self.convert(num1)+self.convert(num2))

    def convert(self,s):
        s = s[::-1]
        count = 0
        for i,v in enumerate(s):
            count +=(ord(v) - ord('0'))*(10**i)

        return count


num1 = '10'
num2 = '222'

test = Solution()
result = test.addStrings(num1,num2)
print(result)
