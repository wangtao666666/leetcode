class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        参考链接：https://blog.csdn.net/qq_21275321/article/details/82977852
        """
        indexs=[i for i,v in enumerate(bin(N)) if v=='1']
        return max([b-a for a ,b in zip(indexs,indexs[1:])] or[0])

N = 22
test = Solution()
result = test.binaryGap(N)
print(result)
