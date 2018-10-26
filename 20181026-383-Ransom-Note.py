# encoding = 'utf-8'

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        c1 = {}
        for a in magazine:
            if a not in c1:
                c1[a] = 1
            else:
                c1[a] += 1

        for a in ransomNote:
            if a in c1:
                c1[a] -= 1
            else:
                return False

        for c in list(c1.values()):
            if c < 0:
                return False

        return True

    """
    import collection
    
    return not collection.Counter(s1) - collection.Counter(s2)
     
    """

s1 = 'a'
s2 = 'b'
test = Solution()
result = test.canConstruct(s1,s2)
print(result)


