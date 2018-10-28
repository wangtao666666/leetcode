# encoding = 'utf-8'


"""
    参考链接：https://blog.csdn.net/zjrn1027/article/details/81188486
"""

class Solution:
    def compress(self,chars):
        """
        :param chars:  List[str]
        :return: int
        """
        n = len(chars)

        i,count = 0,1

        for j in range(1,n+1):
            print('j:',j)

            if j<n and chars[j] == chars[j-1]:
                count +=1
                print('count:',count)

            else:
                chars[i] = chars[j-1]
                i +=1
                if count > 1:
                    for m in str(count):
                        chars[i] = m
                        i +=1
                count = 1

        return i

chars = ['a','a','b','b','c','c','c']
test = Solution()
result = test.compress(chars)
print(result)
