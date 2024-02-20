class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        zero_count = 0
        max_window = 0
        
        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_window = max(max_window, right - left + 1)
        
        return max_window
