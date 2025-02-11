from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newDic = Counter(nums)
        for key, value in newDic.items():  # Use .items() here
            if value > 1:  # Check if the count is greater than 1, not just not equal to 1
                return True # Return True if you find a duplicate
        return False # Return False only if no duplicates were found

sol = Solution()
print(sol.containsDuplicate([1, 1, 2]))  # Output: True
print(sol.containsDuplicate([1, 2, 3]))  # Output: False
print(sol.containsDuplicate([1,2,3,1])) # Output: True