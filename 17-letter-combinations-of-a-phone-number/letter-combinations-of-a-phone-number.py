class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_combination: str):
            if index == len(digits):
                result.append(current_combination)
                return
            
            current_digit = digits[index]
            for letter in digit_to_char[current_digit]:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result
