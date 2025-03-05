class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        if len(arr) % 2 != 0:
            return False

        remainders = {}
        for num in arr:
            remainder = num % k
            remainders[remainder] = remainders.get(remainder, 0) + 1

        for num in arr:
            remainder = num % k
            complement = (k - remainder) % k  

            if remainder == 0:
                if remainders.get(0, 0) % 2 != 0:
                    return False
            elif remainders.get(remainder, 0) != remainders.get(complement, 0):
                return False

        return True