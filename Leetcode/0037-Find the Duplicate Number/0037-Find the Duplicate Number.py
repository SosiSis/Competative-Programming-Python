class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
    



#     nums = [1, 3, 4, 2, 2]
#             ↑  ↑  ↑  ↑  ↑
#     index   0  1  2  3  4
# The value at each index tells you where to go next. So you can treat this array like a "linked list" where:

# index 0 has value 1 → go to index 1

# index 1 has value 3 → go to index 3

# index 3 has value 2 → go to index 2

# index 2 has value 4 → go to index 4

# index 4 has value 2 → go to index 2 (again!)