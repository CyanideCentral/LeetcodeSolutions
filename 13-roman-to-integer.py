class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s)==0:
            return 0
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        i=0
        while True:
            if i==len(s)-1:
                res+=d[s[i]]
                break
            if d[s[i+1]]>d[s[i]]:
                res+=-d[s[i]]
            else:
                res+=d[s[i]]
            i+=1
        return res