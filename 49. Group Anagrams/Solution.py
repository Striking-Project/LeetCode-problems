class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for word in strs:
            char_count = [0] * 26  # Count frequency of each character
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            anagram_groups[tuple(char_count)].append(word)
        
        return list(anagram_groups.values())
