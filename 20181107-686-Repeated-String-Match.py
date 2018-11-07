class Solution(object):
    def repeatedStringMatch(self, A, B):

        """
        :type A: str
        :type B: str
        :rtype: int
        """
        res = A
        count = 1

        while len(res) < len(B):
            res += A
            count += 1

        if res.find(B) != -1:
            return count

        res += A
        if res.find(B) != -1:
            return count + 1

        return -1


