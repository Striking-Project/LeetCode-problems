class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area if necessary
            max_area = max(max_area, current_area)
            
            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                # Skip over any elements smaller than the current height
                next_left = left + 1
                while next_left < right and height[next_left] <= height[left]:
                    next_left += 1
                left = next_left
            else:
                next_right = right - 1
                while next_right > left and height[next_right] <= height[right]:
                    next_right -= 1
                right = next_right
        
        return max_area
