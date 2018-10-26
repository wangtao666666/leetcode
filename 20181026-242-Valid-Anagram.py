# encoding = 'utf-8'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s1 = {}
        for i in s:
            if i not in s1:
                s1[i] = 1
            else:
                s1[i] += 1

        for j in t:
            if j in s1:
                s1[j] -= 1
            else:
                return False

        for item in list(s1.values()):
            if item != 0:
                return False
        return True

s = 'anagram'
t = 'nagaram'
test = Solution()
result = test.isAnagram(s,t)
print(result)



