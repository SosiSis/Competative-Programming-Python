class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:  # Handle empty input
            return ""

        # Use zip to compare characters at the same index across all strings
        for i, chars in enumerate(zip(*strs)): #zip(*strs) transposes the list of strings
            if len(set(chars)) != 1: #check if all the charachters in the tuple are equal
                return strs[0][:i] #if not equal return the prefix from the first string till the unmatched index

        return strs[0]  # If all characters match, the shortest string is the prefix