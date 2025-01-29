# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    # This is just a placeholder; the real function is provided externally.
    pass  


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n > 0:
            low = 1
            high = n

            while low <= high:  
                mid = (low + high) // 2  
                
                if isBadVersion(mid):  
                    high = mid - 1  
                else:
                    low = mid + 1  

            return low  
        
        return -1  
