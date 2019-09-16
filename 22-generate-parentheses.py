def getps(s,n,d):
    if len(s)+d==2*n:
        return [s+d*')']
    res=getps(s+'(',n,d+1)
    if d>0:
        res+=getps(s+')',n,d-1)
    return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return getps('(',n,1)