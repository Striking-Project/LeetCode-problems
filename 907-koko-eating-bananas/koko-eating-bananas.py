class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            hours = 0 
            for pile in piles:
                hours += -(-pile // k) # Same as using math.ceil(pile / k)
            
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

