class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)

        def gcd(a, b):
            """
            Calculates the greatest common divisor of two numbers using Euclid's algorithm.
            Args:
              a: The first number.
              b: The second number.
            Returns:
              The greatest common divisor of a and b.
            """
            while b:
                a, b = b, a % b
            return a

        return gcd(min_num, max_num)