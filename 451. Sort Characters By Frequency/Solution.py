class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1 

        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        sorted_string = ''.join(char * freq_map[char] for char in sorted_chars)

        return sorted_string

        