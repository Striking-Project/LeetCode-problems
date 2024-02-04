class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        The goal is to return the pivot index of the array defined as the element where the sum of
        elements on it's right equates the sum of the ones on it's left.

        Args:
            nums(List[int]):input array.

        Returns:
            int:The pivot index.
        """
        if not(1 <= len(nums) <= 10**4):
            raise ValueError("The size of the input array must be between 1 and 10**4")

        for i in range(len(nums)):
            if not(-1000 <= nums[i] <= 1000):
                raise ValueError("The array elements must be between -1000 and 1000")

        #Calculate the total sum of the array
        total_sum = sum(nums)

        #Initialize the left sum
        left_sum = 0

        #Iterate through the array
        for i in range(len(nums)):
            #Check if the sum of the elements on the left equates the sum on the right
            if left_sum == total_sum - left_sum - nums[i]:
                #Return the pivot index if found
                return i
            
            #Update the left sum for the next iteration 
            left_sum += nums[i]

        #return -1 if no pivot is found
        return -1  