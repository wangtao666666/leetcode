class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        return word.isupper() or word.islower() or word.istitle()



word = 'USA'
test = Solution()
result = test.detectCapitalUse(word)
print(result)