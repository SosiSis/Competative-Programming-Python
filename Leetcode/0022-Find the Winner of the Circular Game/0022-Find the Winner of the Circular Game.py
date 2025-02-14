class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 1

        winner = self.findTheWinner(n - 1, k)
        return (winner + k - 1) % n + 1

# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         friends = list(range(1, n + 1))
#         index = 0
        
#         while len(friends) > 1:
#             index = (index + k - 1) % len(friends)
#             friends.pop(index)
        
#         return friends[0]