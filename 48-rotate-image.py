class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                if i*2-1==n and j**2+1==n:
                    continue
                t=matrix[i][j]
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-1-i]
                matrix[j][n-1-i]=t
        return