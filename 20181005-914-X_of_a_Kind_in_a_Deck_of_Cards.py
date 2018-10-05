# encoding = 'utf-8'

class Solution(object):
    def hasGroupSizeX(self,deck):
        """
        :param deck:
        :return:
        """
        deck.sort()
        x = 2

        while x< len(deck):
            if len(deck)%x!=0:
                x +=1
                continue
            group = int(len(deck)/x)
            flag = True

            for i in range(group):
                if deck[i*x] != deck[x*(i+1)-1]:
                    flag = False
                    break
            if flag:
                return True
            x +=1

        return False

deck = [1,1,2,2,2,2]
test = Solution()
result = test.hasGroupSizeX(deck)
print(result)