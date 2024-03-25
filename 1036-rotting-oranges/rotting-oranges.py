from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while rotten:
            size = len(rotten)
            
            for _ in range(size):
                i, j = rotten.popleft()
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_count -= 1
                        rotten.append((ni, nj))
            
            minutes += 1
        
        return minutes - 1 if fresh_count == 0 else -1
