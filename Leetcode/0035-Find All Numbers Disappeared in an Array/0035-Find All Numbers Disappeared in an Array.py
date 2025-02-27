class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Mark visited numbers by making them negative
        for num in nums:
            index = abs(num) - 1  # Get the index (1-based to 0-based)
            nums[index] = -abs(nums[index])  # Mark as visited
        
        # Step 2: Collect missing numbers (those indices that remain positive)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
