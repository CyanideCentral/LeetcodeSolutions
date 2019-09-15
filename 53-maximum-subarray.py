#O(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res=-2**31
        sum=0
        for i,n in enumerate(nums):
            sum+=n
            if sum>res:
                res=sum
            if sum<0:
                sum=0
        return res