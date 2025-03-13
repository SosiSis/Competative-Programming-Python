from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2:
            return min(height[0], height[1]) * 1

        res=0
        l,r = 0,len(height) -1
        while l < r:
            area =(r-l) * min(height[l],height[r])
            res =max(res,area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  
        return res          



 