# encoding = 'utf-8'

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        """
        参考：https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/convert-a-number-to-hexadecimal.py
        
        """
        if not num:
            return '0'

        result = []

        while num and len(result) != 8:
            h = num & 15
            print('h:',h)
            if h < 10:
                print(ord('0')+h)
                print(chr(ord('0')+h))
                result.append(str(chr(ord('0') + h)))
            else:
                result.append(str(chr(ord('a') + h - 10)))
                print(result)

            num >>= 4
            print(num)

        print(result)
        result.reverse()
        print(result)
        return ''.join(result)


num = 26
test = Solution()
result = test.toHex(num)
print(result)
