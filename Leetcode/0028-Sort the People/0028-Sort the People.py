from collections import defaultdict

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(heights)

        # Bubble Sort (Modified to sort names and heights together)
        for i in range(n):
            for j in range(n - i - 1):
                if heights[j] < heights[j + 1]:  # Sort in descending order of heights
                    # Swap heights
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    # Swap names correspondingly
                    names[j], names[j + 1] = names[j + 1], names[j]

        return names # Return the sorted names