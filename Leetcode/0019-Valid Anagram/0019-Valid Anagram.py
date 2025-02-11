from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
         return False
        hashmap = Counter(s) # TC for Counter is O(n)

        for ch in t:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                return False
        return True
        