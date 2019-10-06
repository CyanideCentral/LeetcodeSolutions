class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        a=1
        b=2
        for i in range(n-2):
            a,b=b,a+b
        return b