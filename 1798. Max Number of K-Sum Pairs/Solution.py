class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        The goal is to find the maximum number of individual combinations of sums that equal k.

        Args:
            nums(List[int]):input list of numbers.
            k(int): input integer to be equated.

        Returns:
            int:The total number of operations.
        """
        if not(1 <= k <= 10**9):
            raise ValueError("k should be between 1 and 10**9")

        for i in range(len(nums)):
            if not(1 <= nums[i] <= 10**9):
                raise ValueError("the numbers in nums should be between 1 and 10**9")
        
        if not(1 <= len(nums) <= 10**5):
            raise ValueError("the size of the list should be between 1 and 10**5")

        #Sort the list for a two-pointer approach
        nums.sort()

        #Initialize pointers
        left, right = 0, len(nums) - 1

        #Number of operations
        operations = 0

        while left < right:
            sum = nums[left] + nums[right]

            if sum == k:
                #Pair found
                operations += 1
                left += 1
                right -= 1

            elif sum < k:
                left += 1
            else:
                right -= 1
        
        return operations


