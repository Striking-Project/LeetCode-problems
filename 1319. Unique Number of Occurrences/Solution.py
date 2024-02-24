class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        count_set = set()
        for count in freq.values():
            if count in count_set:
                return False
            count_set.add(count)
        
        return True
