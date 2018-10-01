#encoding='utf-8'

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (D-B)*(C-A) + (H-F)*(G-E) - max(0,(min(C,G)-max(A,E)))*max(0,(min(D,H)-max(B,F)))

A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
test = Solution()
result = test.computeArea(A=A,B=B,C=C,D = D,E = E,F = F,G = G,H = H)
print(result)