class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            if 2*i==m or 2*i==n:
                return res
            if 2*i+1==m:
                for j in range(i, n-i):
                    res.append(matrix[i][j])
                return res
            if 2*i+1==n:
                for j in range(i, m-i):
                    res.append(matrix[j][i])
                return res
            for j in range(i, n-1-i):
                res.append(matrix[i][j])
            for j in range(i, m-1-i):
                res.append(matrix[j][n-1-i])
            for j in range(n-1-i,i,-1):
                res.append(matrix[m-1-i][j])
            for j in range(m-1-i,i,-1):
                res.append(matrix[j][i])
        return res