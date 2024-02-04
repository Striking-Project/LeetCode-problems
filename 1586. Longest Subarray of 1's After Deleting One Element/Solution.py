class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Returns the size of the longest non-empty subarray containing only 1's.

        Args:
            nums(List[int]):input binary list.

        Returns:
            int: size of the longest noo--empty subarray.    
        """
        
        if not(1 <= len(nums) <= 10**5):
            raise ValueError("the size of list should be between 1 and 10**5")
        
        if not(all(num in [1,0] for num in nums)):
            raise ValueError("The list should be binary")
        
        left, right = 0, 0
        max_length = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left)
            
            right += 1

        return max_length