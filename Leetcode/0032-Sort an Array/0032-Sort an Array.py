class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left_half, right_half):
            left_index = 0
            right_index = 0
            sorted_subarray = []
            
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    sorted_subarray.append(left_half[left_index])
                    left_index += 1
                else:
                    sorted_subarray.append(right_half[right_index])
                    right_index += 1
                    
            sorted_subarray.extend(left_half[left_index:])
            sorted_subarray.extend(right_half[right_index:])
            
            return sorted_subarray
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            
            return merge(left_half, right_half)

        if not nums:
            return []  # Handle empty input

        return mergeSort(0, len(nums) - 1, nums)