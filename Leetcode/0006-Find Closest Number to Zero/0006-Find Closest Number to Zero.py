class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            closestNumber=nums[0]
            for num in nums:
                if abs(num) < abs(closestNumber) :
                
                    closestNumber=num
                elif abs(num)==abs(closestNumber) and num>closestNumber:
                    closestNumber=num     
        return closestNumber    