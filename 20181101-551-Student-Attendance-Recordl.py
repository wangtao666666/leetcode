# encoding ='utf-8'

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        else:
            for i in range(len(s) - 2):
                if s[i:i + 3] == 'LLL':
                    return False

        return True

s = 'PPALLP'
test = Solution()
result = test.checkRecord(s)
print(result)
