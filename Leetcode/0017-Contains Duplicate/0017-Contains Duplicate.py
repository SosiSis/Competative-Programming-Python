from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newDic = Counter(nums)
        for key, value in newDic.items(): 
            if value > 1:  
                return True 
        return False 

