from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1] * len(nums1)
        numsInx={num:i for i ,  num in enumerate(nums1)}
        stack=[]
        for i  in range(len(nums2)):
            cur=nums2[i]   
            while stack and cur > stack[-1]:
                val=stack.pop()
                idx=numsInx[val]
                res[idx]=cur
            if cur in numsInx:
                stack.append(cur)
                
        return res 