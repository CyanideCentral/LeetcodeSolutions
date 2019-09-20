class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign=n
        n=abs(n)
        p=x
        r=1
        while n>0:
            if n%2==1:
                r*=p
            n=n//2
            p=p*p
        if sign<0:
            r=1/r
        return r