class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings by adding their letters in alternating order, starting with word1.

        If a string is longer than the other, append the additional letters onto the end  of
        the merged string.

        Args:
             word1 (str): the first input string.
             word2 (str): the second input string.
        
        Retruns:
            str: the merged string.
        """
        if not(1 <= len(word1) <= 100 and 1 <= len(word2) <= 100):
            raise ValueError("Length of the words must be between 1 and 100")

        if not(all('a' <= char <= 'z' for char in word1) and all('a' <= char <= 'z' for char in word2)):
            raise ValueError("Words must only consist of lowercase english letters")
            
        merged = []
        len_word1, len_word2 = len(word1), len(word2)
        min_len = min(len_word1, len_word2)

        #Merge letters alternatively up to the length of the shorter word
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        
        #Append any remaining letters for the two words
        merged.extend(word1[min_len:])
        merged.extend(word2[min_len:])

        #Join the characters to form the final result
        result = ''.join(merged)
        return result
        

        

        