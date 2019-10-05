def reverse(a, l, r):
    while True:
        if l>=r:
            return
        a[l],a[r]=a[r],a[l]
        r-=1
        l+=1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                break
            if i==0:
                i=-1
        if i>=0:
            for j in range(i+1,len(nums)):
                if nums[j]<=nums[i]:
                    j-=1
                    break
            nums[i],nums[j]=nums[j],nums[i]
        reverse(nums,i+1,len(nums)-1)
        return nums