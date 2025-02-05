class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        shortest_str = min(strs, key=len)  # Find the shortest string
        for i in range(len(shortest_str)):
            char = shortest_str[i]
            for other_str in strs:
                if i >= len(other_str) or other_str[i] != char:
                    return shortest_str[:i]  # Return prefix up to mismatch

        return shortest_str  # If all characters match, shortest is the prefix