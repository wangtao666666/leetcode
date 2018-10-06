# encoding='utf-8'

class Solution(object):
    def generate(self,numRows):
        """
        :param numRows: int
        :return: List[List[int]]
        """

        if numRows == 0:
            return []

        tem = [0,1]
        l = []

        for i in range(numRows):
            rowlist = []
            for j in range(len(tem)-1):
                rowlist.append(tem[j]+tem[j+1])
            l.append(rowlist)
            tem = rowlist[:]
            tem.insert(0,0)
            tem.append(0)

        return l

numRows = 3
test = Solution()
result = test.generate(numRows)
print(result)
