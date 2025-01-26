class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, combination: List[int], remaining: int):
            if len(combination) == k and remaining == 0:
                result.append(combination[:])
                return
            
            if len(combination) > k or remaining < 0:
                return

            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, combination, remaining - i)
                combination.pop()
            
        backtrack(1, [], n)
        return result