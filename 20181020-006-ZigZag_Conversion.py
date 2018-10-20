# encdding = 'utf-8'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)]
        row = 0
        step = 1

        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1

            zigzag[row] += c

            print('row:',row)
            print('zigzag:',zigzag)

            row += step

        return ''.join(zigzag)


s = 'PAYPALISHIRING'
numRows = 3

test = Solution()
result = test.convert(s,numRows)
print(result)

