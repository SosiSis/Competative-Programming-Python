from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       curSum=0
       n=len(nums)

       for i in range(k):
           curSum+=nums[i]

       maxAve=curSum/k 

       for i in range(k,n):
         curSum+=nums[i]
         curSum-=nums[i-k]

         ave=curSum/k
         maxAve=max(maxAve,ave)   
       return maxAve   

        