class Solution:
    def countAndSay(self, n: int) -> str:
        r="1"
        i=1
        while i!=n:
            last=None
            count=0
            new=""
            for j in range(len(r)):
                if j!=0 and r[j]!=last:
                    new+=str(count)+last
                    last=r[j]
                    count=1
                else:
                    last=r[j]
                    count+=1
                if j==len(r)-1:
                    new+=str(count)+last
            i+=1
            r=new
        return r