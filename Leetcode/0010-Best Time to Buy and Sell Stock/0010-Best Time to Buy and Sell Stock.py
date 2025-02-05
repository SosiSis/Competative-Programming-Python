class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')  # Initialize with infinity

        for price in prices:
            min_price = min(min_price, price)  # Track the lowest price seen so far
            profit = price - min_price          # Calculate potential profit
            max_profit = max(max_profit, profit) # Update max_profit if necessary

        return max_profit

sol = Solution()
print(sol.maxProfit([1, 2, 3, 4, 5]))  # Output: 4
print(sol.maxProfit([7,1,5,3,6,4])) # Output:5
print(sol.maxProfit([7,6,4,3,1])) # Output:0