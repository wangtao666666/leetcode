# encoding = 'utf-8'

class Solution(object):
    def fizzBuzz(self,n):
        """
        :param n: int
        :return: List[str]
        """
        # method 1

        # result = []
        # for i in range(1,n+1):
        #     if i%3!=0 and i%5!=0:
        #         result.append(str(i))
        #     elif i%3==0 and i%5!=0:
        #         result.append('Fizz')
        #     elif i%5==0 and i%3!=0:
        #         result.append('Buzz')
        #     else:
        #         result.append('FizzBuzz')
        #
        # return result

        # method 2

        return [str(i) if (i%3!=0 and i%5!=0) else ('Fizz'*(i%3==0) + 'Buzz'*(i%5==0)) for i in range(1,n+1)]

n = 15
test = Solution()
result = test.fizzBuzz(n)
print(result)
