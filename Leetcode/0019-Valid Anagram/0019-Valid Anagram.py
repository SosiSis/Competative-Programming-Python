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

        hashmap = Counter(s)

        for ch in list(t):  # Use list(t) to correctly iterate over Unicode chars
            if hashmap[ch] > 0:
                hashmap[ch] -= 1
            else:
                return False
        return True

# Test cases (including Unicode)
print(Solution().isAnagram("anagram", "nagaram"))  # Output: True
print(Solution().isAnagram("rat", "car"))  # Output: False
print(Solution().isAnagram("你好", "好你"))  # Output: True (Unicode - now works correctly)
print(Solution().isAnagram("你好", "好你啊"))  # Output: False (Unicode)
print(Solution().isAnagram("𐐐", "𐐐")) # Output: True (Unicode surrogate pair)
print(Solution().isAnagram("𐐐", "A")) # Output: False (Unicode surrogate pair)