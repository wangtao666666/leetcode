# encoding='utf-8'

class Solution(object):
    def getRow(self,rowIndex):
        """
        :param rowIndex: int
        :return: List[int]
        """
        numRows = rowIndex + 1

        tem = [0,1]
        l = []

        for i in range(numRows):
            rowList = []
            for j in range(len(tem)-1):
                rowList.append(tem[j]+tem[j+1])
            l.append(rowList)
            tem = rowList[:]
            tem.insert(0,0)
            tem.append(0)

        return l[rowIndex]

rowIndex = 3
test = Solution()
result = test.getRow(rowIndex)
print(result)
