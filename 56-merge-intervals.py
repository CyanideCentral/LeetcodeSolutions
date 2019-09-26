class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        res=[]
        for it in intervals:
            if len(res)==0:
                res.append(it)
                continue
            start=None
            end=None
            left=None
            if res[0][0]>it[1]:
                res=[it]+res
                continue
            if res[0][0]>=it[0]:
                start=0
                left=it[0]
            else:
                for i in range(len(res)):
                    if res[i][1]>=it[0]:
                        start=i
                        left=min(it[0], res[i][0])
                        break
                if start==None:
                    res+=[it]
                    continue
            for i in range(start,len(res)):
                if it[1]<res[i][0]:
                    res=res[0:start]+[[left,it[1]]]+res[i:]
                    end=i-1
                    break
                if it[1]<=res[i][1]:
                    res=res[0:start]+[[left,res[i][1]]]+res[i+1:]
                    end=i
                    break
            if end==None:
                res=res[0:start]+[[left,it[1]]]
        return res