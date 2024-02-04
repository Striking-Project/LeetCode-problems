class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Count the number of pairs of equal column and row.

        Args:
            grid(List[int]): the input grid.
        
        Returns:
            int: the number of pairs.
        """

        # Get the dimensions of the grid
        n = len(grid)
        
        # Check if n satisfies the constraint
        if not (1 <= n <= 200):
            raise ValueError("The size of grid should be between 1 and 200")

        # Check if the elements in the grid satisfy the constraints
        for i in range(n):
            for j in range(n):
                if not (1 <= grid[i][j] <= 10**5):
                    raise ValueError("Grid elements should be between 1 and 10^5")

        # Initialize the count of equal row and column pairs
        equal_pairs_count = 0

        # Iterate over each row and column
        for i in range(n):
            # Check for equal row and column pairs
            for j in range(n):
                # Check if the row and column have the same elements in the same order
                if grid[i] == [grid[k][j] for k in range(n)]:
                    equal_pairs_count += 1

        return equal_pairs_count
