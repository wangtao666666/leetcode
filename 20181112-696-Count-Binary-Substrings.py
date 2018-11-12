# encoding = 'utf-8'

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for i in s.replace("01", "0 1").replace("10", "1 0").split():
            l.append(len(i))

        return sum(min(a, b) for a, b in zip(l, l[1:]))


