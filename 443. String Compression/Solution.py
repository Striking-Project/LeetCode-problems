class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        The goal is to compress a string in a way that retains useful information about it.

        Args:
            chars(list[str]): the input string to be compressed.

        Returns:
            int: the new length of the array after compression.
        """
        
        if not 1 <= len(chars) <= 2000:
            raise ValueError("Invalid length of chars. Should be between 1 and 2000.")

        for char in chars:
            if not isinstance(char, str) or len(char) != 1 or not (char.islower() or char.isupper() or char.isdigit() or char.isascii()):
                raise ValueError("Invalid character in chars. Should be a lowercase/uppercase letter, digit, or symbol.")        
        
        if not chars:
            return 0

        current_char = chars[0]
        count = 1
        index = 0  # Start index at 0

        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                chars[index] = current_char
                index += 1

                if count > 1:
                    for digit in str(count):
                        chars[index] = digit
                        index += 1

                current_char = chars[i]
                count = 1

        chars[index] = current_char
        index += 1

        if count > 1:
            for digit in str(count):
                chars[index] = digit
                index += 1

        return index
