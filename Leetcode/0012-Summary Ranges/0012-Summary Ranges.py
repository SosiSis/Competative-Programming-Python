class Solution(object):
    def summaryRanges(self, nums):
        N = len(nums)
        if N == 0:
            return [] 
        if N == 1:
            return [str(nums[0])] 

        summaryRange = []
        start = 0

        for i in range(N):
            if i < N - 1 and nums[i] + 1 == nums[i + 1]:
                continue  
            else:  
                if start == i:  
                    summaryRange.append(str(nums[start]))
                else:  
                    summaryRange.append(str(nums[start]) + "->" + str(nums[i]))
                start = i + 1  

        return summaryRange

sol = Solution()
print(sol.summaryRanges([1,2,3,4,5,7]))  

