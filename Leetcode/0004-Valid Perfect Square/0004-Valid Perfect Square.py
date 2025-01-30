class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        high=num
        low=1
        while low <= high:
            mid=(high+low ) // 2
            if (mid ** 2) == num:
                return True
            elif (mid ** 2) > num:
                high = mid-1
            else:
                low=mid+1
        return False                

        