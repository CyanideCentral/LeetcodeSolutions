class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s)==0:
            return []
        if len(words)==0:
            return []
        res=[]
        for i in range(len(words[0])):
            res+=self.findSubstring1(s[i:],words, i)
        return res
        
    def findSubstring1(self, s: str, words: List[str], offset: int) -> List[int]:
        l=[]
        d={}
        lw=len(words[0])
        for i in range(len(s)//lw):
            t=s[i*lw:i*lw+lw]
            l.append(t)
        for w in words:
            if w not in d:
                d[w]=1
            else:
                d[w]+=1
        i=0
        res=[]
        td={}
        for t in d:
            td[t]=0
        tl=0
        while i<len(l):
            start=i-tl
            if l[i] not in d:
                for t in d:
                    td[t]=0
                tl=0
            elif td[l[i]]<d[l[i]]:
                td[l[i]]+=1
                tl+=1
                if tl==len(words):
                    res.append(start*lw+offset)
                    td[l[start]]-=1
                    tl-=1
            else:
                j=start
                while j<i:
                    td[l[j]]-=1
                    tl-=1
                    if l[j]==l[i]:
                        break
                    j+=1
                td[l[i]]+=1
                tl+=1
            i+=1
        return res