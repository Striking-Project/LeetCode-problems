import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs) - 1
        min_heap = []
        
        for i in range(candidates):
            if left <= right:
                heapq.heappush(min_heap, (costs[left], left))
                left += 1
        
        for i in range(candidates):
            if left <= right:
                heapq.heappush(min_heap, (costs[right], right))
                right -= 1
        
        total_cost = 0
        while k > 0:
            cost, index = heapq.heappop(min_heap)
            total_cost += cost
            k -= 1
            
            if index < left:
                if left <= right:
                    heapq.heappush(min_heap, (costs[left], left))
                    left += 1
            elif index > right:
                if left <= right:
                    heapq.heappush(min_heap, (costs[right], right))
                    right -= 1
        
        return total_cost
