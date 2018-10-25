# encoding = 'utf-8'

import operator

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)

        return operator.eq(v1, v2)


version1 = '1.1.1'
version2 = '1.0.1'
test = Solution()
result = test.compareVersion(version1,version2)
print(result)


