class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums)==0):
            return [-1,-1]
        t=nums[0]
        if t>target:
            return [-1,-1]
        elif t==target:
            left=0
        else:
            left=self.locate(nums,target-0.5)+1
        if left>=len(nums) or nums[left]!=target:
            return [-1,-1]
        t=nums[-1]
        if t<target:
            return [-1,-1]
        elif t==target:
            right=len(nums)-1
        else:
            right=self.locate(nums,target+0.5)
        return [left,right]
        
    def locate(self, nums:List[int], target:float)->int:
        left=0
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid
            else:
                right=mid
        return left