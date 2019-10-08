class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end=[0,0,0]
        for i in range(len(nums)):
            if nums[i]==0:
                nums[end[2]]=nums[end[1]]
                nums[end[1]]=nums[end[0]]
                nums[end[0]]=0
                end[0]+=1
                end[1]+=1
                end[2]+=1
            elif nums[i]==1:
                nums[end[2]]=nums[end[1]]
                nums[end[1]]=1
                end[1]+=1
                end[2]+=1
            else:
                nums[end[2]]=2
                end[2]+=1