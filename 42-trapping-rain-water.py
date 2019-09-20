class Solution:
    def trap(self, height: List[int]) -> int:
        v0=sum(height)
        maxleft=[]
        for i in height:
            if len(maxleft)==0:
                maxleft.append(i)
            elif maxleft[-1]<i:
                maxleft.append(i)
            else:
                maxleft.append(maxleft[-1])
        maxright=[]
        for i in range(len(height)-1,-1,-1):
            if len(maxright)==0:
                maxright.append(height[i])
            elif maxright[-1]<height[i]:
                maxright.append(height[i])
            else:
                maxright.append(maxright[-1])
        for i in range(1,len(height)-1):
            height[i]=max(height[i],min(maxleft[i-1],maxright[len(height)-i-2]))
        v1=sum(height)
        return v1-v0