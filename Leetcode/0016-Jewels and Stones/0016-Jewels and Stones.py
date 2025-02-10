class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count            

sol=Solution()
print(sol.numJewelsInStones("aA","aachdk"))