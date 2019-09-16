class Solution:
    def intToRoman(self, num: int) -> str:
        d=[['I','V'],['X','L'],['C','D'],['M']]
        res=''
        i=0
        while True:
            if num==0:
                break
            tail=num%10
            if tail==0:
                pass
            elif tail<=3:
                res=d[i][0]*tail+res
            elif tail==4:
                res=d[i][0]+d[i][1]+res
            elif tail==5:
                res=d[i][1]+res
            elif tail<9:
                res=d[i][1]+d[i][0]*(tail-5)+res
            else:
                res=d[i][0]+d[i+1][0]+res
            i+=1
            num=num//10
        return res