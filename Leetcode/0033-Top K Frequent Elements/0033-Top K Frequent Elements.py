class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Count the frequency of each element
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # 2. Create buckets based on frequency
        buckets = [[] for _ in range(len(nums) + 1)] #create buckets from 0 to len(nums)

        # 3. Place elements into buckets based on frequency
        for num, freq in frequency.items():
            buckets[freq].append(num)

        # 4. Gather the k most frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1): #iterate backwards through buckets
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
            