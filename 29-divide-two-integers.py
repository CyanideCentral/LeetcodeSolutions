class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        i=0
        l=len(haystack)-len(needle)
        while i<=l:
            j=i
            k=0
            while True:
                if haystack[j]!=needle[k]:
                    break
                j+=1
                k+=1
                if k==len(needle):
                    return i
            i+=1
        return -1