class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = window_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
