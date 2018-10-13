# encoding = 'utf-8'

class Solution(object):
    def shortestToChat(self,S,C):
        """
        :param S:
        :param C:
        :return:
        """

        S = list(S)
        index = []

        for i in range(len(S)):
            if S[i] == C:
                index.append(i)

        result = []
        for i in range(len(S)):
            distance = [abs(i-item) for item in index]
            result.append(min(distance))

        return result

S = "loveleetcode"
C = 'e'

test = Solution()
result = test.shortestToChat(S,C)
print(result)
