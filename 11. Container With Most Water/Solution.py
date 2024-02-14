class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
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
