class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        entrance_row, entrance_col = entrance
        
        # Build the graph
        graph = {}
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == '.':
                    neighbors = []
                    for dr, dc in directions:
                        r, c = i + dr, j + dc
                        if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.':
                            neighbors.append((r, c))
                    graph[(i, j)] = neighbors
        
        # Perform BFS
        queue = deque([(entrance_row, entrance_col, 0)])  # (row, col, steps)
        visited = set([(entrance_row, entrance_col)])
        
        while queue:
            row, col, steps = queue.popleft()
            
            if (row != entrance_row or col != entrance_col) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                return steps
            
            for neighbor_row, neighbor_col in graph[(row, col)]:
                if (neighbor_row, neighbor_col) not in visited:
                    visited.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col, steps + 1))
        
        return -1
