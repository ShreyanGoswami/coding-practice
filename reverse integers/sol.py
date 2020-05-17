###Given a 32-bit signed integer, reverse digits of an integer.###

class Solution:
    base = 2 ** 31
    MAX = base - 1
    MIN = base * (-1)
    def reverse(self, x: int) -> int:
        if self.MIN < x <= self.MAX :
            x = str(x)
            x = x.rstrip("0")
            if x == '':
                return 0
            if x[0] == '-' :
                x = x[1:]
                res = int('-' + x[::-1])
            else :
                res = int(x[::-1])
            if self.MIN < res <= self.MAX :
                return res
            else :
                return 0
        else :
            return 0

sol = Solution()
# print(sol.reverse(0))
print(sol.reverse(1534236469))