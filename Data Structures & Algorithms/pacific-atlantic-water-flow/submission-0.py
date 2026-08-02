class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        #first row pac

        def dfs(row, col, visited, prev_height):

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if (row, col) in visited:
                return
            if heights[row][col] < prev_height:
                return
            
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            #all directions
        for c in range(cols):
                dfs(0, c, pacific, heights[0][c])
                dfs(rows-1, c, atlantic, heights[rows-1][c])
                

            
        for r in range(rows):
                dfs(r, 0, pacific, heights[r][0])
                dfs(r, cols-1, atlantic, heights[r][cols-1])
        res = []
        for cell in pacific & atlantic:
            res.append(cell)
        return res