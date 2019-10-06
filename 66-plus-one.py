class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t=[1]*n
        for i in range(m-1):
            for j in range(n-1):
                t[j+1]+=t[j]
        return t[-1]