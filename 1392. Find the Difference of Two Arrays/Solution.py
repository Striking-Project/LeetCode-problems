class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1 = {}
        freq2 = {}
        
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
        
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1
        
        difference1 = []
        difference2 = []
        
        for num in freq1:
            if num not in freq2:
                difference1.append(num)
        
        for num in freq2:
            if num not in freq1:
                difference2.append(num)
        
        return [difference1, difference2]
