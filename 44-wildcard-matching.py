class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            return True if len(s)==0 else False
        if p[0]=='?':
            if len(s)==0:
                return False
            return self.isMatch(s[1:],p[1:])
        elif p[0]!='*':
            if len(s)==0 or s[0]!=p[0]:
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            while len(p)>1 and p[1]=="*":
                p=p[1:]
            minl=0
            if len(p)==1:
                return True
            for i in range(len(p)):
                if p[i]!="*":
                    minl+=1
            if len(s)==0:
                return True if minl==0 else False
            if len(s)<minl:
                return False
            p=p[1:]
            if '*' not in p:
                locs=self.loc(s,p)
                return True if len(locs)>0 and locs[-1]+len(p)==len(s) else False
            t=p.index('*')
            key=p[0:t]
            locs=self.loc(s,key)
            if len(locs)==0:
                return False
            return self.isMatch(s[(locs[0]+t):],p[t:])
    def loc(self,s,k):
        res=[]
        for i in range(len(s)-len(k)+1):
            for j in range(len(k)):
                if k[j]=='?' or k[j]==s[i+j]:
                    if j==len(k)-1:
                        res.append(i)
                    continue
                else:
                    break
        return res