class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        self.visited = {}

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in self.visited and grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] == "0" or (row, col) in self.visited:
            return

        self.visited[(row, col)] = True

        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)