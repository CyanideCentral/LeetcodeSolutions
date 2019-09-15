class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            if len(s)==0:
                return True
            else:
                return False
        if len(p)==1 or p[1]!='*':
            if len(s)==0:
                return False
            if p[0]!='.' and s[0]!=p[0]:
                return False
            else:
                return self.isMatch(s[1:],p[1:])
        if p[0]=='.':
            for i in range(0,len(s)+1):
                if self.isMatch(s[i:], p[2:]):
                    return True
            return False
        else:
            for i in range(0, len(s)+1):
                if self.isMatch(s[i:], p[2:]):
                    return True
                if i>=len(s) or s[i]!=p[0]:
                    break
            return False
        return False