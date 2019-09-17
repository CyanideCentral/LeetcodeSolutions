class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        h=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[h]=nums[i]
                h+=1
        return h