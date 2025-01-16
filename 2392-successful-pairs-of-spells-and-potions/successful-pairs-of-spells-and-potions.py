class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            required_potion = (success + spell - 1) // spell 
            
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] < required_potion:
                    left = mid + 1
                else:
                    right = mid - 1
            
            count = m - left 
            result.append(count)
        
        return result
