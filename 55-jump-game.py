class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                return True
            if nums[i]==0:
                j=i
                while j>=0:
                    if nums[j]+j>i:
                        break
                    j-=1
                if j<0:
                    return False
                i=i+1
            i=i+nums[i]
        return True
            