class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to store the index of each element in arr2.
    # This will be used for the custom comparator.
        rank = {val: i for i, val in enumerate(arr2)}

        def custom_comparator(x):
            """
            Custom comparator function.
            Elements present in arr2 are ranked based on their index in arr2.
            Elements not in arr2 are ranked based on their value.
            """
            if x in rank:
                return rank[x]  # Return the rank if in arr2
            else:
                return len(arr2) + x # Return a higher rank + the value if not in arr2. This ensures elements not in arr2 are at the end and in ascending order.

        arr1.sort(key=custom_comparator)  # Sort arr1 using the custom comparator
        return arr1

