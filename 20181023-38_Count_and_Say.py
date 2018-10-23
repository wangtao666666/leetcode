# encoding = 'utf-8'


class Solution:
    def countAndSay(self,n):
        """
        :param n:
        :return:
        """

        b = '1'

        for i in range(n-1):
            a,c,count = b[0],'',0

            for j in b:
                if a == j:
                    count +=1
                else:
                    c +=str(count) + a
                    a = j
                    count =1

            c += str(count) + a
            b = c

        return b

n  = 1
test = Solution()
result = test.countAndSay(n)
print(result)
