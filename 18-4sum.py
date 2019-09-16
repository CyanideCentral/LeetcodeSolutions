class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d={}
        res=[]
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                t=nums[i]+nums[j]
                if t in d:
                    d[t].append([i,j])
                else:
                    d[t]=[[i,j]]
        s=d.keys()
        for i in sorted(s):
            if i>target//2:
                break
            if i*2==target:
                for j in range(len(d[i])-1):
                    for k in range(j+1,len(d[i])):
                        if d[i][j][0] in d[i][k] or d[i][j][1] in d[i][k]:
                            continue
                        t=[nums[d[i][j][0]],nums[d[i][j][1]],nums[d[i][k][0]],nums[d[i][k][1]]]
                        t.sort()
                        if t not in res:
                            res.append(t)
                break
            if target-i not in s:
                continue
            for j in d[i]:
                for k in d[target-i]:
                    if j[0] in k or j[1] in k:
                        continue
                    t=[nums[j[0]],nums[j[1]],nums[k[0]],nums[k[1]]]
                    t.sort()
                    if t not in res:
                        res.append(t)
        return res