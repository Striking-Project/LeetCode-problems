class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the largest string x that divides both str1 and str2.

        Args:
            str1(str): the first input string.
            str2(str): the second input string.

        Returns:
            str: the greatest common divider of strings
        """
        
        if not(1 <= len(str1) <= 1000 and 1 <= len(str2) <= 1000):
            raise ValueError("The length of the strings should be between 1 and 1000")
        
        if not(all('A' <= char <= 'Z' for char in str1) and all('A' <= char <= 'Z' for char in str1)):
            raise ValueError("str1 and str2 should consist of only uppercase English letters")

        # Choose the longer string between str1 and str2 based on their lengths
        s1 = max(str1, str2, key=lambda x: len(x))

        if s1 == str1:
            s2 = str2
        else:
            s2 = str1

        #Get the lengths of the two strings
        a1, a2 = len(s1), len(s2)

        #Check if s2, repeated (a1//a2) times, equals s1
        if s2 * (a1 // a2) == s1:
            return s2

        #Iterate over all possible divisors
        for i in range(2, a2 // 2 + 1):
            if(a2 / i) % 1 == 0:
                if s2[:a2 // i] * i == s2:
                    if s1[:a2 // i] * int(i * a1 / a2) == s1:
                        if s1[:a2 // i] == s2[:a2 // i]:
                            return s2[:a2 // i]
        
        #Check if s1 and s2 consist of only 1 repeated character
        if s1.count(s1[0]) == a1 and s2.count(s2[0]) == a2 and s1[0] == s2[0]:
            return s1[0]
        
        #if no common divisor is found return an empty string
        return ""


