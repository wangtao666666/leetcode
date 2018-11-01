# encoding = 'utf-8'


class Solution(object):
    def reverseWords(self,s):
        words = [item[::-1] for item in s.split(' ')]

        return ' '.join(words)



s = "Let's take LeetCode contest"
test = Solution()
result = test.reverseWords(s)
print(result)