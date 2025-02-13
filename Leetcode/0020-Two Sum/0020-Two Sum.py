class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in h:
                return [i, h[y]]
            else:
                h[x] = i