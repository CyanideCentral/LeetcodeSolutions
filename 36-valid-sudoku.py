class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            l=[]
            for j in range(9):
                s=board[i][j]
                if s!=".":
                    if s in l:
                        return False
                    l.append(s)
        for i in range(9):
            l=[]
            for j in range(9):
                s=board[j][i]
                if s!=".":
                    if s in l:
                        return False
                    l.append(s)
        for i in range(3):
            for j in range(3):
                l=[]
                for x in range(3):
                    for y in range(3):
                        s=board[i*3+x][j*3+y]
                        if s!=".":
                            if s in l:
                                return False
                            l.append(s)
        return True