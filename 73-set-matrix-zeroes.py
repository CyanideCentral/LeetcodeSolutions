class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowz=set()
        colz=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rowz.add(i)
                    colz.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowz or j in colz:
                    matrix[i][j]=0