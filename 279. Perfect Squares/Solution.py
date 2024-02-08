class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        perfect_squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        queue = deque([(n, 0)])
        visited = set()
        
        while queue:
            num, level = queue.popleft()
            for square in perfect_squares:
                diff = num - square
                if diff == 0:
                    return level + 1
                elif diff > 0 and diff not in visited:
                    queue.append((diff, level + 1))
                    visited.add(diff)
        
        return -1  # If no solution found

