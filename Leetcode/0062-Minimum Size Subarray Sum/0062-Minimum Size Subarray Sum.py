from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        l=0
        curSum=0
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                res=min(res,r-l+1)
                curSum-=nums[l]
                l+=1
               
        return 0 if res==float("inf") else res