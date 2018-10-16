# encoding = 'utf-8'

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        data = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                data[5] += 1
            elif bill == 10:
                if data[5] == 0:
                    return False
                else:
                    data[10] += 1
                    data[5] -= 1
            elif bill == 20:
                if data[10] != 0:
                    if data[5] == 0:
                        return False
                    else:
                        data[5] -= 1
                        data[10] -= 1
                else:
                    if data[5] < 3:
                        return False
                    else:
                        data[5] -= 3
        return True
    

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
test = Solution()
result = test.lemonadeChange(bills)
print(result)