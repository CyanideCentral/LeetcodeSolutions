def ap(d,tc):
    for k in d:
        if d[k]<tc[k]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc={}
        count={}
        for i in range(len(t)):
            count[t[i]]=0
            if t[i] in tc:
                tc[t[i]]+=1
            else:
                tc[t[i]]=1
        wl=None
        wr=None
        minl=len(s)
        ml=0
        mr=len(s)-1
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
                if wl==None:
                    wl=i
                    if len(t)==1:
                        return t
                elif wr==None:
                    if ap(count,tc):
                        wr=i
                        minl=wr-wl+1
                        ml=wl
                        mr=wr
                if wr!=None:
                    wr=i
                    for j in range(wl,wr+1):
                        if s[j] in count:
                            if count[s[j]]==tc[s[j]]:
                                wl=j
                                if wr-wl+1<minl:
                                    minl=wr-wl+1
                                    ml=wl
                                    mr=wr
                                break
                            else:
                                count[s[j]]-=1
        if wr==None:
            return ""
        return s[ml:mr+1]