# encoding='utf-8'

"""
    详细解析参考链接：https://blog.csdn.net/weixin_41362649/article/details/79884854
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0


n = 10
test = Solution()
result = test.canWinNim(n)
print(result)
