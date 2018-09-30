# encoding='utf-8'

"""
    Question 709:To_Lower_Case
    Description:将大写字母转化小写
    @author:wt
    Created at 2018-09-30

"""
class Solution:
    def toLowerCase(self,str):
        """
        :param str:
        :return:
        """
        return str.lower()


sss = "Hello"

test = Solution()
result = test.toLowerCase(sss)

print(result)