# encoding = 'utf-8'


class Solution(object):
    def reverseStr(self,s,k):
        """
        :param s:
        :param k:
        :return:
        """
        s = list(s)

        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)

s = 'abcd'
k = 2

test = Solution()
result = test.reverseStr(s,k)
print(result)