import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        paired = list(zip(nums2, nums1))
        paired.sort(reverse=True, key=lambda x: x[0])

        min_heap = []  
        current_sum = 0
        max_score = 0

        for num2, num1 in paired:
            heapq.heappush(min_heap, num1)
            current_sum += num1

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
