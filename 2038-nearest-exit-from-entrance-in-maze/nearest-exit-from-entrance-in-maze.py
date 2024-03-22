from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        entrance_row, entrance_col = entrance
        
        queue = deque([(entrance_row, entrance_col, 0)])  # (row, col, steps)
        maze[entrance_row][entrance_col] = '#'  # Mark entrance as visited
        
        while queue:
            row, col, steps = queue.popleft()
            
            if (row != entrance_row or col != entrance_col) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                return steps
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.':
                    maze[r][c] = '#'  # Mark cell as visited
                    queue.append((r, c, steps + 1))
        
        return -1
