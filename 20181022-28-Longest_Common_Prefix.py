# encoding = 'utf-8'

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        for i in range(len(strs[0])):
            for strings in strs[1:]:
                if i > len(strings) or strings[i] != strs[0][i]:
                    return strs[0][:i]


        return strs[0]


        # if not strs:
        #     return ""
        #
        # for i in range(len(strs[0])):
        #     print('i:',i)
        #     for string in strs[1:]:
        #         print('string:',string)
        #         if i >= len(string) or string[i] != strs[0][i]:
        #             return strs[0][:i]
        #
        # return strs[0]


strs = ['flower','flow','flight']
test = Solution()
result = test.longestCommonPrefix(strs)

print(result)
